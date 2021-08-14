from django import forms
from .models import Owner,Company


class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = '__all__'

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'