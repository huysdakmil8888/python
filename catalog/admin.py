from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Product, Image, Slider
from django.urls import path
class CatalogAdminSite(admin.AdminSite):
    site_header = 'Administration System'
    site_title = 'Catalog Admin'
    index_title = 'Catalog Admin Home'
    index_template = 'admin/index.html'
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            # add your custom URLs here
        ]
        return custom_urls + urls

admin_site = CatalogAdminSite()

class CategoryInline(admin.TabularInline):  # or admin.StackedInline
    model = Product.categories.through
    extra = 1  # how many rows to show
    verbose_name_plural = "Categories list"

class ImageInline(admin.TabularInline):  # or admin.StackedInline
    model = Image
    extra = 1  # how many rows to show
    verbose_name_plural = "Image library"
    readonly_fields = ('image_display',)  # add this line
    def image_display(self, obj):
        return format_html('<img src="{}" width="50" height="50" />', obj.pic.url)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'display_image')  # fields to display in list view
    list_filter = ('category',)  # fields to filter by
    search_fields = ('name',)  # fields to search by
    # ordering = ('name',)  # default ordering
    raw_id_fields = ('parent',)  # fields to display as raw id fields

    def display_image(self, obj):
        return format_html('<img src="{}" width="50" height="50" />', obj.image.url)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        # custom queryset
        queryset = queryset.filter()
        return queryset

class ProductAdmin(admin.ModelAdmin):
    inlines = [CategoryInline, ImageInline]
    class Media:
        js = ('js/admin.js',)  # replace 'admin.js' with the actual path to your JavaScript file
    exclude = ('categories',)
    list_display = ('name', 'display_image')  # fields to display in list view
    list_filter = ('name',)  # fields to filter by
    search_fields = ('name',)  # fields to search by
    # ordering = ('name',)  # default ordering
    raw_id_fields = ('categories',)  # fields to display as raw id fields

    def display_image(self, obj):
        return format_html('<img src="{}" width="50" height="50" />', obj.image.url)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        # custom queryset
        queryset = queryset.filter()
        return queryset
        
class ImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'product')  # fields to display in list view

    def image(self, obj):
        return format_html('<img src="{}" width="50" height="50" />', obj.pic.url)

admin_site.register(Category, CategoryAdmin)
admin_site.register(Product, ProductAdmin)
admin_site.register(Image, ImageAdmin)
admin_site.register(Slider)