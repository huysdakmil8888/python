from django.contrib import admin

# Register your models here.
from .models import User
from catalog.admin import admin_site
from django.contrib.auth.models import Group, Permission

admin_site.register(User)
admin_site.register(Group)
admin_site.register(Permission)
