# serializers.py
from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    parent_hierarchy = serializers.SerializerMethodField()
    product_count = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = '__all__'  # or list the fields you want to include
    
    # def get_parent(self, obj):
    #     return obj.parent.name if obj.parent else None
    def get_parent_hierarchy(self, obj):
        hierarchy = []
        def get_parents(category):
            if category.parent:
                hierarchy.append(category.parent.name)
                get_parents(category.parent)
        get_parents(obj)
        return ' -> '.join(reversed(hierarchy))
    def get_product_count(self, obj):
        return obj.products.count()

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = 'name', 'content'
class CommentSerializer(serializers.ModelSerializer):
    replies = ReplySerializer(many=True, read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'  # or list the fields you want to include
        extra_kwargs = { #build-in validation
            'name': {'required': True, 'min_length': 2},
        }
    def validate_comment(self, value): #custom validation
        """Check that content is not empty"""
        if len(value) < 5:
            raise serializers.ValidationError("Content cannot be less than 5 charaters.")
        return value

class ProductSerializer(serializers.ModelSerializer):
    comments_count = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = '__all__'  # or list the fields you want to include
    def get_comments_count(self, obj):
        return obj.comments.count()

