# accounts/urls.py
from django.urls import path

from .views import SignUpView,SignUpAPIView


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('api/signup/', SignUpAPIView.as_view(), name='api_signup'),
]