from django.shortcuts import render
from .models import *


# Create your views here.
def dashboard(request):
    sliders = Slider.objects.all()
    return render(request, 'dashboard.html', locals())
def pro(request):
    return render(request, 'LetsShop/pages/pro/pro.html')
