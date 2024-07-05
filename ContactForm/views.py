from django.shortcuts import render, redirect
from .models import About
from .forms import ContactForm


def about_me(request):
    about = About.objects.all().order_by('-updated_on').first()
    contact_form = ContactForm()

    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "contact_form": contact_form
        },
    )

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')  # Redirect to the thank you page after submission
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def thank_you_view(request):
    return render(request, 'thank_you.html')
