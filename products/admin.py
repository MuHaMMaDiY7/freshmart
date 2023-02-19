from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import ProductModel, ProductTagModel, CategoryModel, ProductColorModel
from .forms import ColorForm


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'real_price', 'price', 'discount']
    list_display_links = ['id', 'title', 'real_price', 'price', 'discount']
    list_filter = ['created_at']
    search_fields = ['title']
    readonly_fields = ['real_price']


@admin.register(ProductColorModel)
class ProductColorModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'code', 'get_code', 'name']
    list_display_links = ['id', 'code', 'get_code', 'name']
    search_fields = ['code', 'name']
    form = ColorForm

    def get_code(self, obj):
        text = '&nbsp;' * 10
        return mark_safe(f'<p style="background-color:{obj.code}; width:100px;">{text}</p>')


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    list_filter = ['created_at']
    search_fields = ['name']


@admin.register(ProductTagModel)
class ProductTagModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']
