import random

from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from .models import Product, ProductCategory


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)[:3]
    return same_products


def get_hot_product():
    products = Product.objects.all()

    return random.sample(list(products), 1)[0]


def products(request, pk=None):
    title = 'продукты'
    # links_menu = [
    #     {'href': 'index', 'name': 'все'},
    #     {'href': 'products_home', 'name': 'дом'},
    #     {'href': 'products_office', 'name': 'офис'},
    #     {'href': 'products_modern', 'name': 'модерн'},
    #     {'href': 'products_classic', 'name': 'классика'},
    # ]
    links_menu = ProductCategory.objects.all()
    basket = get_basket(request.user)

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)

    # basket = []
    # if request.user.is_authenticated:
    #     basket = Basket.objects.filter(user=request.user)

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        context = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products,
            'related_products': same_products,
            'basket': basket,
            'hot_product': hot_product,
        }
        return render(request, 'mainapp/products.html', context)

    products = Product.objects.all().order_by('price')

    context = {
        'title': title,
        'links_menu': links_menu,
        'related_products': same_products,
        'products': products,
        'basket': basket,
        'hot_product': hot_product,
    }
    return render(request, 'mainapp/products.html', context)


def product(request, pk):
    title = 'продукты'
    links_menu = ProductCategory.objects.all()
    basket = get_basket(request.user)

    product = get_object_or_404(Product, pk=pk)

    same_products = get_same_products(product)

    context = {
        'title': title,
        'links_menu': links_menu,
        'related_products': same_products,
        'basket': basket,
        'product': product,
    }
    return render(request, 'mainapp/product.html', context)
