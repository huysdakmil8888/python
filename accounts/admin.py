from django.contrib import admin

# Register your models here.
from .models import User
# from catalog.admin import admin_site
from django.contrib.auth.models import Permission
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from django.contrib.auth.forms import UserCreationForm as DefaultUserCreationForm
from django import forms


admin.site.register(User)
admin.site.register(Permission)
