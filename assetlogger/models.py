from django.db import models
from django.utils import timezone


class Asset(models.Model):
    """ Asset details. """
    asset_name = models.CharField(max_length=200)
    ext_url = models.URLField(max_length=200)


class AssetInstance(models.Model):
    """ Individual asset record. """
    asset = models.ForeignKey('Asset', on_delete=models.CASCADE)
    date = models.ForeignKey('AssetDate', on_delete=models.CASCADE)
    unit = models.CharField(max_length=20, choices=[('USD', 'USD')])
    value = models.DecimalField(decimal_places=2, max_digits=20)


class AssetDate(models.Model):
    """ Date of asset log. Used to aggregate assets on a date. """
    date = models.DateField('Date of asset data', default=timezone.now)
