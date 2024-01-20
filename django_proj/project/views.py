from django.shortcuts import render
from .models import Product
from django.utils import timezone

def product_list(request):
    products = Product.objects.all()
    current_datetime = timezone.now()
    is_sale_active = True

    context = {
        'products': products,
        'current_datetime': current_datetime,
        'is_sale_active': is_sale_active
    }
    return render(request, 'project/products_list.html', context)