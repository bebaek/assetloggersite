from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from assetlogger.forms import CreateAssetInstanceForm
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

            # FIXME: Redirect to date view instead
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
