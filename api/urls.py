from django.urls import path, include
from .views import BookListView
from catalog.views import *
from rest_framework import routers
from catalog.views import *

router = routers.DefaultRouter()
router.register('categories', CategoryViewSet, basename='category')
router.register('comments', CommentViewSet)
# router.register('reports', ReportViewSet, basename='report')

urlpatterns = [
    path('', include(router.urls)),
    path('reports/', ReportViewSet.as_view()),
    # path('hello/', BookListView.as_view(), name='hello'),
]
