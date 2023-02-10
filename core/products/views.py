from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Product, Category


class LandingView(View):
    def get(self, request, category_id=None):
        products = Product.objects.filter(available=True)
        categories = Category.objects.filter(parent__isnull=True)
        if category_id:
            category = Category.objects.get(id=category_id)
            products = products.filter(categories=category)
        return render(request, 'product/home.html', {'products': products, 'categories': categories})


class ProductDetailView(View):
    def get(self, request, id):
        product = get_object_or_404(Product, id=id)
        return render(request, 'product/detail.html', {'product': product})
