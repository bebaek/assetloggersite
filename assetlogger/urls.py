from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('asset_instance/create', views.create_asset_instance,
         name='create_asset_instance'),
    path('asset_date/create', views.create_asset_date,
         name='create_asset_date'),
]
