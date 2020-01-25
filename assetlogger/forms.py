from django import forms

from .models import Asset, AssetDate


class CreateAssetInstanceForm(forms.Form):
    asset = forms.ModelChoiceField(queryset=Asset.objects.all())
    date = forms.ModelChoiceField(queryset=AssetDate.objects.all())
    unit = forms.CharField()
    value = forms.DecimalField(decimal_places=2, max_digits=20)


class CreateAssetDateForm(forms.Form):
    date = forms.DateField()
