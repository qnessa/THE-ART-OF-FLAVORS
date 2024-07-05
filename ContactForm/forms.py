from .models import ContactRequest 
from django import forms

#Custom model form start here


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactRequest
        fields = ['name', 'email', 'subject', 'message']
