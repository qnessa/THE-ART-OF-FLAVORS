from django import forms
from .models import Contactform
#Custom model form start here


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contactform
        fields = ['name', 'email', 'subject', 'message']
