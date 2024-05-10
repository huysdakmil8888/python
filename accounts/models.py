from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    # email = models.EmailField()
    # password = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True, unique=True)
    image = models.ImageField(upload_to='users/%Y/%m', null=True, blank=True)
    # first_name = models.CharField(max_length=100)
    # last_name = models.CharField(max_length=100)
    # phone = models.CharField(max_length=100)
    # address = models.CharField(max_length=100)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.username
    def get_image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return 'https://gravatar.com/avatar/12ebd360d20871ec4308b7447c46f928?s=400&d=robohash&r=x'