from django.db import models
from django.utils import timezone


class Asset(models.Model):
    """ Asset details. """
    asset_name = models.CharField(max_length=200)
    ext_url = models.URLField(max_length=200)

    def __str__(self):
        return f'{self.asset_name}'


class AssetInstance(models.Model):
    """ Individual asset record. """
    asset = models.ForeignKey('Asset', on_delete=models.CASCADE)
    date = models.ForeignKey('AssetDate', on_delete=models.CASCADE)
    unit = models.CharField(max_length=20, choices=[('USD', 'USD')])
    value = models.DecimalField(decimal_places=2, max_digits=20)

    def __str__(self):
        asset_str = self.asset.asset_name
        date_str = str(self.date.date)
        return f'{asset_str} on {date_str}'


class AssetDate(models.Model):
    """ Date of asset log. Used to aggregate assets on a date. """
    date = models.DateField('Date of asset data', default=timezone.now)

    def __str__(self):
        return f'{self.date}'
