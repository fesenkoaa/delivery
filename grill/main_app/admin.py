from django.core.exceptions import ValidationError
from django.forms import ModelChoiceField, ModelForm
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

from PIL import Image


class HelpMessageAdminForm(ModelForm):

    MIN_RESOLUTION = (450, 300)
    MAX_RESOLUTION = (3600, 2400)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].help_text = mark_safe("<span style='color:red; font-size:12px;'>"
                                                   "The resolution of image must be {} x {}"
                                                   "</span>".format(*self.MIN_RESOLUTION))

    def clean_image(self, *args, **kwargs):
        image = self.cleaned_data['image']
        if image:
            img = Image.open(image)
            min_height, min_width = self.MIN_RESOLUTION
            max_height, max_width = self.MAX_RESOLUTION
            if img.height < min_height or img.width < min_width:
                raise ValidationError('Image should be bigger!')
            if img.height > max_height or img.width > max_width:
                raise ValidationError('Image should be smaller!')
            return image


class ProductAdmin(admin.ModelAdmin):

    form = HelpMessageAdminForm
    prepopulated_fields = {'slug': ('title'.lower(), )}


class CategoryAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('name'.lower(),)}


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)