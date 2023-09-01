from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib import messages
from django.db.models import Q

# Create your views here.
def dashboard(request):
    user     = request.user
    if user:
        cart = Cart.objects.filter(user=user)
        cart_len = len(cart)
        if cart:
            total = 0
            for i in cart:
                total_amount = (i.quantity) * (i.product.current_price)
                total = total + total_amount

    sliders  = Slider.objects.all()
    products = Product.objects.all()
    featured = products.filter(featured_product=True)
    trending = products.filter(trending_product=True)
    deal     = products.filter(deals_of_the_day=True)
    top_sell = products.filter(top_seller=True)
    return render(request, 'dashboard.html', locals())

def SSCatProduct(request, id):
    super_cat = Super_SubCategory.objects.get(id=id)
    user = request.user
    if user:
        cart = Cart.objects.filter(user=user)
        cart_len = len(cart)
        if cart:
            total = 0
            for i in cart:
                total_amount = (i.quantity) * (i.product.current_price)
                total = total + total_amount
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

def add_to_cart(request, id):
    user = request.user
    product_cart = Product.objects.get(id=id)
    if user.is_authenticated:
        try:
            cart = Cart.objects.get(Q(user=user, product=product_cart))
            cart.quantity += 1
            cart.save()
            return redirect('dashboard')
        except Cart.DoesNotExist:
            cart = Cart.objects.create(user=user, product=product_cart)
            cart.save()
            return redirect('dashboard')
def remove_cart(request, id):
    user = request.user
    cart = Cart.objects.get(Q(user=user, id=id))
    cart.delete()
    return redirect('dashboard')

def cart_page(request):
    user = request.user
    if user:
        cart = Cart.objects.filter(user=user)
        cart_len = len(cart)
        if cart:
            total = 0
            shipping_charge = 75.00
            for i in cart:
                total_amount = (i.quantity) * (i.product.current_price)
                total = total + total_amount
                ship_total = total + 75
    return render(request, 'LetsShop/pages/cart/cart_page.html', locals())















def pro(request):
    return render(request, 'LetsShop/pages/pro/pro.html')
