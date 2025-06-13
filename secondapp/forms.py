from django import forms
from secondapp.models import contact

class ContactForms(forms.ModelForm):
    class Meta:
        model = contact
        fields = ("first_name", "last_name", "email", "phone_no", "address", "message")