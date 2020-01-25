from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('assets/', views.AssetListView.as_view(), name='assets'),
    path('asset/create', views.create_asset, name='create-asset'),
    path('asset-instance/create', views.create_asset_instance,
         name='create-asset-instance'),
    path('asset_date/create', views.create_asset_date,
         name='create-asset-date'),
]
