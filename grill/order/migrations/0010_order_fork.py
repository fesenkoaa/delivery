# Generated by Django 3.2.9 on 2022-02-07 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_alter_order_order_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='fork',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]