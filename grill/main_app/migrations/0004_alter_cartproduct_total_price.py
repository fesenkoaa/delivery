# Generated by Django 3.2.9 on 2021-12-06 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_cart_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartproduct',
            name='total_price',
            field=models.IntegerField(verbose_name='Total price'),
        ),
    ]
