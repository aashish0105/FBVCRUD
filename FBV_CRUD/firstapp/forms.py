from django import forms
from .models import Laptop
class LaptopModelForm(forms.ModelForm):
    Purchasedate = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model=Laptop
        fields='__all__'