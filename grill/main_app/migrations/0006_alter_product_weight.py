# Generated by Django 3.2.9 on 2021-12-06 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20211206_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.IntegerField(blank=True, null=True, verbose_name='Weigh'),
        ),
    ]