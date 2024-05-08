# accounts/views.py
from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts.models import User
from .forms import CustomUserCreationForm
from rest_framework import generics
from .serializers import SignUpSerializer
from rest_framework.parsers import MultiPartParser
from .signals import user_signed_up

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        return response

class SignUpAPIView(generics.CreateAPIView):
    serializer_class = SignUpSerializer
    parser_classes = [MultiPartParser]
    def perform_create(self, serializer):
        user = serializer.save()
        user_signed_up.send(sender=self.__class__, user_id=user.id)

