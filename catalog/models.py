# categories/models.py

from django.db import models
import os
from PIL import Image as PilImage
from io import BytesIO
from django.core.files import File

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def delete(self, *args, **kwargs):
        print('image',self.image.path)
        if os.path.isfile(self.image.path):
            os.remove(self.image.path)
        super().delete(*args, **kwargs)

class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')
    categories = models.ManyToManyField(Category, related_name='products')

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


class Image(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    pic = models.FileField(upload_to='products/')
