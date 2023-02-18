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
        # context['min'], context['max'] = ProductModel.objects.all().aggregate(Min('real_price'), Max('real_price')).values()
        return context
        #

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
        return qs
