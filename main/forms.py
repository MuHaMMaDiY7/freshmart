from django import forms
from .models import ContactMessageModel


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessageModel
        exclude = ['created_at']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Name'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email'
            }),
            'theme': forms.TextInput(attrs={
                'placeholder': 'Subject'
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Message'
            })
        }