from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from main_app.models import Product
from .cart import SessionCart
from .forms import CartAddProductForm
from django.contrib import messages


@require_POST
def cart_add(request, product_id):
    cart = SessionCart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    try:
        qty = int(request.POST.get('quantity'))
    except ValueError:
        messages.error(request, 'Ilość musi być bez liter!')
        return redirect('main_app:main')
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 # quantity=cd['quantity'],
                 quantity=qty,
                 update_quantity=cd['update'])
    return redirect('cart:session-cart')


def cart_update(request, product_id):
    cart = SessionCart(request)
    product = get_object_or_404(Product, id=product_id)
    qty = int(request.POST.get('quantity'))
    cart.update(product=product,
                quantity=qty)
    return redirect('cart:session-cart')


def cart_remove(request, product_id):
    cart = SessionCart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:session-cart')


def cart_detail(request):
    cart = SessionCart(request)
    return render(request, 'session-cart.html', {'cart': cart})