from timeit import default_timer

from django.contrib.auth.models import Group
from django.http import HttpRequest
from django.shortcuts import render

from .models import Product

def view_shop_index(request: HttpRequest) -> render:
    products = [
        ('Laptop', 1999),
        ('Desktop', 2999),
        ('Smartphone', 9999)
    ]

    context = {
        'time_running': default_timer(),
        'products': products,
    }
    return render(request, 'shopapp/shop-index.html', context=context)


def view_groups_list(request: HttpRequest) -> render:
    context = {
        'groups': Group.objects.prefetch_related('permissions').all(),
    }
    return render(request, 'shopapp/groups_list.html', context=context)

def view_products_list(request:HttpRequest) -> render:
    context = {

        'products': Product.objects.all(),

    }
    return render(request, 'shopapp/products-list.html', context=context)