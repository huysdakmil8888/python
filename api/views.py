# views.py
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Book
from .serializers import *
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated

class BookListView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        # Lấy tất cả các cuốn sách từ cơ sở dữ liệu
        books = Book.objects.all()
        
        # Serialize danh sách các cuốn sách
        serializer = BookSerializer(books, many=True)
        
        # Trả về danh sách các cuốn sách dưới dạng JSON
        return Response('he')
    
    def post(self, request):
        # Lấy tất cả các cuốn sách từ cơ sở dữ liệu
        books = Author.objects.all()
        
        # Serialize danh sách các cuốn sách
        serializer = AuthorSerializer(books, many=True)
        
        # Trả về danh sách các cuốn sách dưới dạng JSON
        return Response(serializer.data)
