# serializers.py
from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    parent = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = '__all__'  # or list the fields you want to include
    
    def get_parent(self, obj):
        return obj.parent.name if obj.parent else None
    
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'  # or list the fields you want to include
    