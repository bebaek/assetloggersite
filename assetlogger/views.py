from django.views import generic
from django.http import HttpResponse

from assetlogger.models import AssetDate


def index(request):
    return HttpResponse('Hello, world')


class AssetDateListView(generic.ListView):
    model = AssetDate
