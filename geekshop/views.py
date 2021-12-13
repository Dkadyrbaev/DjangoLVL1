from django.shortcuts import render

from basketapp.models import Basket


def index(request):
    title = 'главная'

    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    context = {
        'title': title,
        'basket': basket,
    }
    return render(request, 'geekshop/index.html', context)


def contacts(request):
    title = 'контакты'

    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    context = {
        'title': title,
        'basket': basket,
    }
    return render(request, 'geekshop/contact.html', context)


