# urls.py

from django.urls import path
from catalog.views import *

urlpatterns = [
    path('categories', category_list, name='category_list'),
    path('categories/<int:pk>/', category_detail, name='category_detail'),
    path('categories/create/', category_create, name='category_create'),
    path('categories/<int:pk>/update/', category_update, name='category_update'),
    path('categories/<int:pk>/delete/', category_delete, name='category_delete'),

    path('products', product_list, name='product_list'),
    path('products/<int:pk>/', product_detail, name='product_detail'),
    path('products/create/', product_create, name='product_create'),
    path('products/<int:pk>/update/', product_update, name='product_update'),
    path('products/<int:pk>/delete/', product_delete, name='product_delete'),

    path('reports/', report_list, name='reports'),

]
