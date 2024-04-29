# categories/forms.py

from django import forms
from .models import Category,Product,Image
from django.forms import modelformset_factory
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'image', 'parent']

class ProductForm(forms.ModelForm):
    # content = forms.CharField(widget=CKEditorUploadingWidget)
    class Meta:
        model = Product
        fields = '__all__'

ImageFormSet = modelformset_factory(Image, fields=('pic',), extra=1)