from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
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
    date_strs = [ad.date.isoformat() for ad in asset_dates]

    # Get asset instances matching dates and get total values
    assets = [
        AssetInstance.objects.filter(date=ad) for ad in asset_dates]
    values = map(lambda x: sum([a.value for a in x]), assets)

    context = {'value_history': zip(date_strs, values)}

    return render(request, 'index.html', context=context)


class AssetListView(LoginRequiredMixin, generic.ListView):
    model = Asset


class AssetUpdate(LoginRequiredMixin, generic.edit.UpdateView):
    model = Asset
    fields = '__all__'


class AssetDelete(LoginRequiredMixin, generic.edit.DeleteView):
    model = Asset
    success_url = reverse_lazy('assets')


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
def create_asset_instance(request):
    # POST: process the form data
    if request.method == 'POST':
        form = CreateAssetInstanceForm(request.POST)

        if form.is_valid():
            asset_instance = AssetInstance(
                asset=form.cleaned_data['asset'],
                date=form.cleaned_data['date'],
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
                'date': Asset.objects.get(pk=1),
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
