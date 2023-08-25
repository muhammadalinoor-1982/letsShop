
from django.urls import path
from .views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('SSCatProduct/<id>/', SSCatProduct, name='SSCatProduct'),
    path('search/', search, name='search'),
    path('pro/', pro, name='pro')
]
