from django import http
from django.shortcuts import render
from .models import Product
from django.http import HttpResponse


def product_list(request):
    product = Product.objects.all()
    return render(request, 'gallery/index.html', {'products': product})


def home(request):
    return HttpResponse('Hello, World!')
