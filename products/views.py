from django.db.models import Min, Max
from django.shortcuts import render
from django.views.generic import ListView
from .models import ProductModel, CategoryModel, ProductColorModel, ProductTagModel


class ProductListView(ListView):
    template_name = 'main/product-grid-left-sidebar.html'
    model = ProductModel
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CategoryModel.objects.all()
        context['tags'] = ProductTagModel.objects.all()
        context['colors'] = ProductColorModel.objects.all()
        context['min'], context['max'] = ProductModel.objects.all().aggregate(Min('price'), Max('price')).values()
        return context

    def get_queryset(self):
        qs = ProductModel.objects.all()
        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(title__icontains=q)

        cat = self.request.GET.get('cat')
        if cat:
            qs = qs.filter(category=cat)

        tag = self.request.GET.get('tag')
        if tag:
            qs = qs.filter(tags=tag)

        color = self.request.GET.get('color')
        if color:
            qs = qs.filter(colors=color)

        price = self.request.GET.get('price')
        if price:
            price = price.split(';')
            qs = qs.filter(real_price__gte=price[0], real_price__lte=price[1])
        sort = self.request.GET.get('sort')
        if sort:
            qs = qs.order_by(sort)

        return qs
