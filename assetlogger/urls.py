from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path(
        'asset_history/', views.AssetDateListView.as_view(),
        name='asset_history'),
]
