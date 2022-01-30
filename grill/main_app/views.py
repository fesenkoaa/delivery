from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db import transaction
from django.contrib.contenttypes.models import ContentType
from django.contrib import messages
from django.views import View
from django.views.generic import DetailView
from django.contrib.auth import authenticate, login, logout

from cart.cart import SessionCart

from .models import *
from .mixins import *
from .forms import *
from .utils import recalc_cart

from cart.forms import CartAddProductForm


class BaseView(View):

    def get(self, request):
        page_obj = Product.objects.all().order_by('-updated_at')[:8]
        cart_product_form = CartAddProductForm()
        cart = SessionCart(request)
        context = {
            "cart_product_form": cart_product_form,
            'cart': cart,
            'page_obj': page_obj,
        }

        return render(request, 'base.html', context)


class AboutPage(View):

    def get(self, request):
        return render(request, 'about.html')


class ContactPage(View):

    def get(self, request):
        return render(request, 'contact.html')


class Detail(DetailView):

    def get_context_data(self, request, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = self.cart  # added
        return context


class AllDishes(View):

    def get(self, request):
        page_obj = Product.objects.all().order_by('-updated_at')
        cart_product_form = CartAddProductForm()
        cart = SessionCart(request)
        context = {
            "page_obj": page_obj,
            "cart_product_form": cart_product_form,
            "cart": cart
        }

        return render(request, 'all_dishes.html', context)


class MainDishesPage(View):

    def get(self, request):
        page_obj = Product.objects.filter(category=1).order_by('-updated_at')
        cart_product_form = CartAddProductForm()
        cart = SessionCart(request)
        context = {
            'page_obj': page_obj,
            "cart_product_form": cart_product_form,
            "cart": cart
        }

        return render(request, 'main_dishes.html', context)


class SaladsPages(View):

    def get(self, request):
        page_obj = Product.objects.filter(category=2).order_by('-updated_at')
        cart_product_form = CartAddProductForm()
        cart = SessionCart(request)
        context = {
            'page_obj': page_obj,
            "cart_product_form": cart_product_form,
            "cart": cart
        }

        return render(request, 'salads.html', context)


class AdditivesPage(View):

    def get(self, request):
        page_obj = Product.objects.filter(category=4).order_by('-updated_at')
        cart_product_form = CartAddProductForm()
        cart = SessionCart(request)
        context = {
            'page_obj': page_obj,
            "cart_product_form": cart_product_form,
            "cart": cart
        }

        return render(request, 'additives.html', context)


class SousPage(View):

    def get(self, request):
        page_obj = Product.objects.filter(category=5).order_by('-updated_at')
        cart_product_form = CartAddProductForm()
        cart = SessionCart(request)
        context = {
            'page_obj': page_obj,
            "cart_product_form": cart_product_form,
            "cart": cart
        }

        return render(request, 'sous.html', context)


class DrinksPage(View):

    def get(self, request):
        page_obj = Product.objects.filter(category=3).order_by('-updated_at')
        cart_product_form = CartAddProductForm()
        cart = SessionCart(request)
        context = {
            'page_obj': page_obj,
            "cart_product_form": cart_product_form,
            "cart": cart
        }

        return render(request, 'drinks.html', context)


class CartPage(View):

    def get(self, request):
        print(request.session)
        return render(request, 'session_cart.html')
