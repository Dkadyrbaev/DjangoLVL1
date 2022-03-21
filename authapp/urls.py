from django.contrib import admin
from django.urls import path
from .views import login, logout, register, edit
admin.autodiscover()

app_name = 'authapp'

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register'),
    path('edit/', edit, name='edit')
]
