# serializers.py
from rest_framework import serializers
from .models import Author, Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'publication_year']

class AuthorSerializer(serializers.ModelSerializer):
    author = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'author']
