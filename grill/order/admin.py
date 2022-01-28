from django.contrib import admin
from .models import Order, OrderItem

'''
Мы используем ModelInline для модели OrderItem, чтобы включить ее в качестве inline встроенного в класс OrderAdmin.
Inline режим позволяет включить модель для отображения на той же странице редактирования, что и родительская модель.
'''


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'city', 'address', 'paid',
                    'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)