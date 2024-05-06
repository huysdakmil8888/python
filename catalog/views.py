# categories/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import CategoryForm,ProductForm,ImageFormSet
from django.core.paginator import Paginator
from .signals import categories_retrieved
from rest_framework import viewsets,generics
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count
import logging
class CategoryViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # pagination_class = 'rest_framework.pagination.PageNumberPagination'

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    @action(detail=True, methods=['get']) # add custom route
    def product_comments(self, request, pk=None):
        comments = Comment.objects.filter(product_id=pk).order_by('-id')
        serializer = self.get_serializer(comments, many=True)
        return Response(serializer.data)
class ReportViewSet(generics.ListCreateAPIView):
    # permission_classes = (IsAuthenticated,)
    def list(self, request, *args, **kwargs):
        queryset = Category.objects.all()
        serializer =  CategorySerializer(queryset, many=True)

        queryset2 = Product.objects.all().order_by('-view')[:5]
        serializer2 = ProductSerializer(queryset2, many=True)

        queryset3 = Product.objects.annotate(comments_count=Count('comments')).order_by('-comments_count')[:5]
        serializer3 = ProductSerializer(queryset3, many=True)
        return Response({
            'categories': serializer.data,
            'top_viewed_products': serializer2.data,
            'top_commented_products': serializer3.data
        })


def report_list(request):
    return render(request, 'reports/reports.html')    
def category_list(request):
    categories = Category.objects.all()
    paginator = Paginator(categories, 10)

    page_number = request.GET.get('page')
    categories = paginator.get_page(page_number)
    categories_retrieved.send(categories=categories,sender=category_list)
    return render(request, 'categories/category_list.html', {'categories': categories})

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'categories/category_detail.html', {'category': category})

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'categories/category_add.html', {'form': form})

def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'categories/category_add.html', {'form': form})

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'categories/category_confirm_delete.html', {'category': category})

def product_list(request):
    products = Product.objects.all()
    paginator = Paginator(products, 10)

    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
    return render(request, 'products/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.view += 1
    product.save()
    return render(request, 'products/product_detail.html', {'product': product})

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        formset = ImageFormSet(request.POST, request.FILES, queryset=Image.objects.none())
        if form.is_valid() and formset.is_valid():
            product = form.save()
            for f in request.FILES.getlist('pic'):
                Image.objects.create(pic=f, product=product)
            return redirect('product_list')
    else:
        form = ProductForm()
        formset = ImageFormSet(queryset=Image.objects.none())
    return render(request, 'products/product_add.html', {'form': form, 'formset': formset})

def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save()
            for f in request.FILES.getlist('pic'):
                Image.objects.create(pic=f, product=product)
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
        print('product', product)
        formset = ImageFormSet(queryset=Image.objects.filter(product=product))
    return render(request, 'products/product_add.html', {'form': form, 'formset': formset})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'products/product_confirm_delete.html', {'product': product})