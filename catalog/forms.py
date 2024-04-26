# categories/forms.py

from django import forms
from .models import Category,Product,Image
from django.forms import modelformset_factory

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'image', 'parent']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'image', 'categories']

ImageFormSet = modelformset_factory(Image, fields=('pic',), extra=1)