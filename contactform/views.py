from django.shortcuts import render, redirect
from .models import Contactform
from .forms import ContactForm
from django.http import HttpResponse
#Custom model form start hear

def contactform(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Thank you, your contact form is received! I endeavor to respond within 2 working days.') 

        
    else:
        form = Contactform()
        return render(request, 'contactform/contactform.html', {'form': form})
   

