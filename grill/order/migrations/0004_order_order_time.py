# Generated by Django 3.2.9 on 2022-01-28 08:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_order_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_time',
            field=models.TimeField(default=datetime.datetime(2022, 1, 28, 10, 58, 36, 618221)),
        ),
    ]
