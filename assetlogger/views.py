from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import generic

from assetlogger.models import AssetDate, AssetInstance


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


class AssetDateListView(generic.ListView):
    model = AssetDate

    def get_context_data(self, **kwargs):
        """ Return custom context with [date, value] list. """
        context = super().get_context_data(**kwargs)
        asset_dates = context['assetdate_list']
        date_strs = [ad.date.isoformat() for ad in asset_dates]

        # Get asset instances matching dates and get total values
        assets = [
            AssetInstance.objects.filter(date=ad) for ad in asset_dates]
        values = map(lambda x: sum([a.value for a in x]), assets)

        return {'value_history': zip(date_strs, values)}
