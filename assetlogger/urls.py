from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('assets/', views.AssetListView.as_view(), name='assets'),
    path('asset/create/', views.create_asset, name='create-asset'),
    path('asset/<int:pk>/update/', views.AssetUpdate.as_view(),
         name='update-asset'),
    path('asset/<int:pk>/delete/', views.AssetDelete.as_view(),
         name='delete-asset'),
    path('asset-date/create/', views.create_asset_date,
         name='create-asset-date'),
    path('asset-date/<int:pk>', views.AssetDateDetail.as_view(),
         name='asset-date-detail'),
    path('asset-instance/create/<int:pk_date>', views.create_asset_instance,
         name='create-asset-instance'),
]
