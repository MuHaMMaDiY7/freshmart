from django.contrib import admin
from .models import BannerModel


@admin.register(BannerModel)
class BannerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'status']
    list_display_links = ['id']