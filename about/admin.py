from django. contrib import admin
from .models import About, ContactRequest
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    
    summernote_fields = ('content')
    list_display = ('Title', 'content', 'updated_on')
    search_fields = ['title', 'content']
    list_filter = ['updated_on']

@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):

    list_display = ('message', 'read')
    
