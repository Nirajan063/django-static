from django import forms
from .models import country, provience

class CountryForm(forms.ModelForm):
    class Meta:
        model = country
       # fields = "__all__"
        fields=("country_name","country_code","continent")

class ProvinceForm(forms.ModelForm):
    class Meta:
        model = provience
        fields = ("provience_name",)
