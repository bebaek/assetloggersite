from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.db.models import Sum
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic

from assetlogger.forms import (
    CreateAssetForm, CreateAssetDateForm, CreateAssetInstanceForm
)
from assetlogger.models import Asset, AssetDate, AssetInstance


@login_required
def index(request):
    asset_dates = AssetDate.objects.all()

    value_history = []
    for ad in asset_dates:
        # Get asset instances matching dates and get total values
        value = AssetInstance.objects.filter(date=ad).aggregate(Sum('value'))

        # Build a list of (pk, date, value) for context
        value_history += [(ad.pk, ad.date.isoformat(), value['value__sum'])]

    context = {'value_history': value_history}
    return render(request, 'index.html', context=context)


class AssetListView(LoginRequiredMixin, generic.ListView):
    model = Asset


class AssetUpdate(LoginRequiredMixin, generic.edit.UpdateView):
    model = Asset
    fields = '__all__'


class AssetDelete(LoginRequiredMixin, generic.edit.DeleteView):
    model = Asset
    success_url = reverse_lazy('assets')


class AssetDateDetail(LoginRequiredMixin, generic.DetailView):
    model = AssetDate

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        asset_instance_list = AssetInstance.objects.filter(
            date=context['object'])

        names = []
        values = []
        for ai in asset_instance_list:
            names += [ai.asset.asset_name]
            values += [ai.value]
        context['asset_instance_details'] = zip(names, values)
        return context


@login_required
def create_asset(request):
    # POST: process the form data
    if request.method == 'POST':
        form = CreateAssetForm(request.POST)

        if form.is_valid():
            asset = Asset(
                asset_name=form.cleaned_data['asset_name'],
                ext_url=form.cleaned_data['ext_url'],
            )
            asset.save()
            return HttpResponseRedirect(reverse('index'))

    # GET: create the default form
    else:
        form = CreateAssetForm()

    context = {
        'form': form,
    }
    return render(request, 'assetlogger/create_asset.html', context)


@login_required
def create_asset_instance(request, pk_date):
    asset_date = AssetDate(pk=pk_date)

    # POST: process the form data
    if request.method == 'POST':
        form = CreateAssetInstanceForm(request.POST)

        if form.is_valid():
            asset_instance = AssetInstance(
                asset=form.cleaned_data['asset'],
                date=asset_date,
                unit=form.cleaned_data['unit'],
                value=form.cleaned_data['value'],
            )
            asset_instance.save()
            return HttpResponseRedirect(reverse('index'))

    # GET: create the default form
    else:
        form = CreateAssetInstanceForm(
            initial={
                'asset': Asset.objects.get(pk=1),
                'date': asset_date,
                'unit': 'USD',
            })

    context = {
        'form': form,
    }
    return render(request, 'assetlogger/create_asset_instance.html', context)


@login_required
def create_asset_date(request):
    # POST: process the form data
    if request.method == 'POST':
        form = CreateAssetDateForm(request.POST)

        if form.is_valid():
            asset_date = AssetDate(
                date=form.cleaned_data['date'],
            )
            asset_date.save()
            return HttpResponseRedirect(reverse('index'))

    # GET: create the default form
    else:
        default_date = AssetDate().date  # Initial date defined in model
        form = CreateAssetDateForm(
            initial={
                'date': default_date,
            })

    context = {
        'form': form,
    }
    return render(request, 'assetlogger/create_asset_date.html', context)
