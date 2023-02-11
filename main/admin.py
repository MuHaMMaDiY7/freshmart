from django.contrib import admin
from .models import BannerModel, ContactMessageModel


@admin.register(BannerModel)
class BannerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'status']
    list_display_links = ['id']

@admin.register(ContactMessageModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['name']
    readonly_fields = ["name", "email", "theme", "message"]
