from django.contrib import admin
from catalog.admin import admin_site
from .models import Book, Author


admin_site.register(Book)
admin_site.register(Author)