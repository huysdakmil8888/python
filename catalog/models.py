# categories/models.py
import sys
from django.contrib.auth.models import AbstractUser
from django.db import models
import os
from PIL import Image as PilImage
from io import BytesIO
from django.core.files import File
from ckeditor.fields import RichTextField

class itemBase(models.Model): # abstract base class
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True

class Category(itemBase):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='categories/%Y/%m', null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=False)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return str(self.name)
    def get_image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return ''  # replace with the path to your default image
    
    def delete(self, *args, **kwargs):
        print('image',self.image.path)
        if os.path.isfile(self.image.path):
            os.remove(self.image.path)
        super().delete(*args, **kwargs)

class Product(itemBase):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')
    categories = models.ManyToManyField(Category, related_name='products')
    view = models.IntegerField(default=0)
    content = RichTextField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    def delete(self, *args, **kwargs):
        print('image',self.image.path)
        if os.path.isfile(self.image.path):
            os.remove(self.image.path)
        super().delete(*args, **kwargs)
    
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # save thumbnail
        if self.image: 
            img = PilImage.open(self.image.path)
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                thumb_io = BytesIO()
                img.save(thumb_io, img.format)
                file_name = self.image.name.split('/')[-1]

                self.image.save(
                    file_name,
                    File(thumb_io),
                    save=False,
                )

        super().save(*args, **kwargs)


class Image(itemBase):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    pic = models.FileField(upload_to='products/')
class Comment(itemBase):
    name = models.CharField(max_length=100)
    comment = models.TextField(max_length=100)
    product = models.ForeignKey(Product, related_name='comments', on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.name
    

class Reply(itemBase):
    name = models.CharField(max_length=100)
    content = models.TextField(max_length=100)
    comment = models.ForeignKey(Comment, related_name='replies', on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.name
    
class Slider(itemBase):
    image = models.ImageField(upload_to='slider/')
    description = models.CharField(max_length=100)
    def __str__(self):
        return self.description