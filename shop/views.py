from django.shortcuts import render
from .models import Product

# Create your views here.
def catalogue(request):
    all_products = Product.objects.all();
    return render(request, 'shop/catalogue.template.html',{
        'all_products':all_products
    })