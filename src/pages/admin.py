from django.contrib import admin

from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number', 'message', 'created_at', 'updated_at')

admin.site.register(Contact, ContactAdmin)
