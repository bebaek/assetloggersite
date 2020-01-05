from django.contrib import admin

from .models import Asset, AssetDate, AssetInstance

admin.site.register(Asset)
admin.site.register(AssetDate)
admin.site.register(AssetInstance)
