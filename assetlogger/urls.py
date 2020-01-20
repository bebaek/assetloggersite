from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_asset_instance/', views.create_asset_instance,
         name='create_asset_instance'),
]
