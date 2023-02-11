from django.contrib import admin
from .models import BlogModel, CommentModel


@admin.register(BlogModel)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    search_fields = ['title']
    list_filter = ['created_at']

@admin.register(CommentModel)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['body']
