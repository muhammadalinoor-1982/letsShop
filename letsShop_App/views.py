from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib import messages
from django.db.models import Q

# Create your views here.
def dashboard(request):
    sliders = Slider.objects.all()
    products = Product.objects.all()
    featured = products.filter(featured_product=True)
    trending = products.filter(trending_product=True)
    return render(request, 'dashboard.html', locals())

def SSCatProduct(request, id):
    super_cat = Super_SubCategory.objects.get(id=id)
    superCat_Product = Product.objects.filter(super_subcategory=id)
    return render(request, 'LetsShop/pages/cat_product/product.html', locals())

def search(request):
    try:
        form            = ProductSearchForm(request.GET)
        products        = Product.objects.all()

        if form.is_valid():
            query             = form.cleaned_data.get('query')
            category          = form.cleaned_data.get('category')
            subcategory       = form.cleaned_data.get('subcategory')
            super_subcategory = form.cleaned_data.get('super_subcategory')
            size              = form.cleaned_data.get('size')
            color             = form.cleaned_data.get('color')
            condition         = form.cleaned_data.get('condition')

            if query:
                product = products.objects.filter(Q(title__icontains=query))
            if category:
                product = products.filter(category=category)
            if subcategory:
                product = products.filter(subcategory=subcategory)
            if super_subcategory:
                product = products.filter(super_subcategory=super_subcategory)
            if size:
                product = products.filter(size=size)
            if color:
                product = products.filter(color=color)
            if condition:
                product = products.filter(condition=condition)

    except Exception as e:
        messages.error(request, 'Product Not Available')
    return render(request, 'search/product/product_search.html', locals())

















def pro(request):
    return render(request, 'LetsShop/pages/pro/pro.html')
