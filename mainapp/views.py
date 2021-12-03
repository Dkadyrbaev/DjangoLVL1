from django.shortcuts import render
from .models import Product, ProductCategory


def index(request):
    title = 'каталог'
    # links_menu = [
    #     {'href': 'index', 'name': 'все'},
    #     {'href': 'products_home', 'name': 'дом'},
    #     {'href': 'products_office', 'name': 'офис'},
    #     {'href': 'products_modern', 'name': 'модерн'},
    #     {'href': 'products_classic', 'name': 'классика'},
    # ]
    links_menu = ProductCategory.objects.all()

    rel_products = Product.objects.all()[:4]

    context = {
        'title': title,
        'links_menu': links_menu,
        'related_products': rel_products
    }
    return render(request, 'mainapp/products.html', context)
