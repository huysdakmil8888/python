from django.urls import path, include
from .views import BookListView
from catalog.views import *
from rest_framework import routers
from catalog.views import *

router = routers.DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('comments', CommentViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('hello/', BookListView.as_view(), name='hello'),
]
