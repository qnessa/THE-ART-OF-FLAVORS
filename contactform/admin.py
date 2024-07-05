from django.contrib import admin
from .models import Contactform



# Register your models here.

@admin.register(Contactform)
class ContactformAdmin(admin.ModelAdmin):  
    list_display = ('name', 'email', 'message', 'subject') 