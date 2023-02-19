from django import forms
from .models import ProductColorModel


class ColorForm(forms.ModelForm):
    code = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'color'
    }))

    class Meta:
        model = ProductColorModel
        fields = ['code', 'name']