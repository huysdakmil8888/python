from django.db.models.signals import post_save, pre_delete, post_delete
from django.dispatch import receiver, Signal
from .models import Category
from accounts.models import User
import os

# Define custom signals
category_created = Signal()
category_deleted = Signal()
categories_retrieved = Signal()

@receiver(categories_retrieved)
def handle_categories_retrieved2(sender, categories, **kwargs):
    print('xin chao', sender)
# Define receivers for custom signals
@receiver(category_created)
def handle_category_created(sender, instance, created, **kwargs):
    print(f"Category created: {instance.name}")

@receiver(category_deleted)
def handle_category_deleted(sender, instance, **kwargs):
    print(f"Category deleted: {instance.name}")
    if os.path.isfile(instance.image.path):
        os.remove(instance.image.path)

@receiver(post_save, sender=Category)
def post_save_category(sender, instance, created, **kwargs):
    print('category save!')

@receiver(post_delete, sender=Category)
def post_delete_category(sender, instance, **kwargs):
    print('category delete!')

