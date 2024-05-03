from django.urls import path
from .views import BookListView
from catalog.views import *

urlpatterns = [
    path('hello/', BookListView.as_view(), name='hello'),
    path('categories/', categoryList.as_view()),
    path('categories/<int:pk>/delete/', CategoryDelete.as_view(), name='category-delete'),
    path('comments/', CommentCreate.as_view()),
    path('product/comment/<int:pk>', ProductCommentView.as_view()),


]
