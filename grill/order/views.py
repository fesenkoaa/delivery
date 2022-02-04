from django.shortcuts import render, redirect
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import SessionCart
from order.config import token, chat_id
from django.contrib import messages
import datetime
import requests


def order_create(request):
    cart = SessionCart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()

            message_string = ""
            order_num = ""

            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])

                order_num = f'{order}'
                message_string += f'{item["product"]} ({item["quantity"]} шт.) {item["price"]} zl. \n'

            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            order_type = form.cleaned_data['order_type']
            city = form.cleaned_data['city']
            address = form.cleaned_data['address']
            message = form.cleaned_data['message']

            time = datetime.datetime.now()
            time = time.strftime("%H:%M")

            msg = f'ДОСТАВКА \n\n' \
                f'гость: {first_name} {last_name} \n' \
                f'телефон: {phone} \n' \
                f'email: {email} \n' \
                f'адрес: {city}, {address}\n' \
                f'тип доставки: {order_type}\n' \
                f'время: {time}\n\n\n' \
                f'{order_num}:\n' \
                f'{message_string} \n' \
                f'счет: {cart.get_total_price()} zl.\n\n' \
                f'сообщение: \n{message}'

            requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={msg}')
            print(f'    echo:  {order_num}')

            # empty cart
            cart.clear()
            cart = SessionCart(request)
            # return render(request, 'created.html',
            #               {'order': order, 'cart': cart})
            messages.success(request, 'Twoje zamówienie w trakcie realizacji!')
            return redirect('main_app:main')
    else:
        form = OrderCreateForm
        cart = SessionCart(request)
    return render(request, 'create.html',
                  {'cart': cart, 'form': form})
