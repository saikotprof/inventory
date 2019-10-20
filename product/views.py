from django.shortcuts import render
from .models import Apple, Samsung, Xiaomi, Mobile


def index(request):
    return render(request, 'index.html')


def product(request):
    items = Mobile.objects.all()
    context = {
        'items': items,
        'header': 'Products Page',
    }
    return render(request, 'inventory/products.html', context)


def apple(request):
    items = Apple.objects.all()
    context = {
        'items': items,
        'header': 'Apple',
    }
    return render(request, 'inventory/products.html', context)


def samsung(request):
    items = Samsung.objects.all()
    context = {
        'items': items,
        'header': 'Samsung',
    }
    return render(request, 'inventory/products.html', context)


def xiaomi(request):
    items = Xiaomi.objects.all()
    context = {
        'items': items,
        'header': 'Xiaomi',
    }
    return render(request, 'inventory/products.html', context)
