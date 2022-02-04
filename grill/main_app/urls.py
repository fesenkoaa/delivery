from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *

urlpatterns = [
    path('', BaseView.as_view(), name='main'),
    path('about-us/', AboutPage.as_view(), name='about'),
    path('contact-us/', ContactPage.as_view(), name='contact'),
    path('comments/', CommentPage.as_view(), name='comments'),
    path('main/', AllDishes.as_view(), name='all-dishes'),
    path('main-dishes/', MainDishesPage.as_view(), name='main-dishes'),
    path('salads/', SaladsPages.as_view(), name='salads'),
    path('additives/', AdditivesPage.as_view(), name='additives'),
    path('souses/', SousPage.as_view(), name='sous'),
    path('drinks/', DrinksPage.as_view(), name='drinks'),
]
