# Generated by Django 3.2.9 on 2022-01-28 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_order_order_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_time',
        ),
    ]
