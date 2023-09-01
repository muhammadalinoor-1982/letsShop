
from django.urls import path
from .views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('SSCatProduct/<id>/', SSCatProduct, name='SSCatProduct'),
    path('search/', search, name='search'),
    path('add_to_cart/<id>/', add_to_cart, name='add_to_cart'),
    path('remove_cart/<id>/', remove_cart, name='remove_cart'),
    path('cart_page/', cart_page, name='cart_page'),
    path('pro/', pro, name='pro')
]
