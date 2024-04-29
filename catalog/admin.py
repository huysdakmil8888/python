from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Product, Image

class CategoryInline(admin.TabularInline):  # or admin.StackedInline
    model = Product.categories.through
    extra = 0  # how many rows to show
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'display_image')  # fields to display in list view
    list_filter = ('category',)  # fields to filter by
    search_fields = ('name',)  # fields to search by
    # ordering = ('name',)  # default ordering
    raw_id_fields = ('parent',)  # fields to display as raw id fields

    def display_image(self, obj):
        return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        display_image.short_description = 'Image'

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        # custom queryset
        queryset = queryset.filter()
        return queryset

class ProductAdmin(admin.ModelAdmin):
    inlines = [CategoryInline]
    exclude = ('categories',)
    list_display = ('name', 'display_image')  # fields to display in list view
    list_filter = ('name',)  # fields to filter by
    search_fields = ('name',)  # fields to search by
    # ordering = ('name',)  # default ordering
    raw_id_fields = ('categories',)  # fields to display as raw id fields

    def display_image(self, obj):
        return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        display_image.short_description = 'Image'

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        # custom queryset
        queryset = queryset.filter()
        return queryset
        
class ImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'product')  # fields to display in list view

    def image(self, obj):
        return format_html('<img src="{}" width="50" height="50" />', obj.pic.url)
        image.short_description = 'Image'

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Image, ImageAdmin)