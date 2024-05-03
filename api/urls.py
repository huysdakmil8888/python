from django.urls import path
from .views import BookListView

urlpatterns = [
    path('hello/', BookListView.as_view(), name='hello'),
]
