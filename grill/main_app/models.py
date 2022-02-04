from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone

User = get_user_model()


class Category(models.Model):

    name = models.CharField(max_length=255, verbose_name='Categories')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Product(models.Model):

    category = models.ForeignKey(Category, verbose_name='Category', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Name')
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name='IMG')
    description = models.TextField(max_length=255, null=True, verbose_name='Description')
    weight = models.IntegerField(verbose_name='Weigh', null=True, blank=True)
    price = models.IntegerField(verbose_name='Price')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"

    def get_model_name(self):
        return self.__class__.__name__.lower()

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


class Comment(models.Model):

    email = models.EmailField()
    auth = models.CharField(max_length=50)
    message = models.CharField(max_length=500)
    date = models.DateField(auto_now_add=True)
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = '-time',
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return f'{self.auth} add a new comment'






