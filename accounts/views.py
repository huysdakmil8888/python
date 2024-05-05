# accounts/views.py
from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts.models import User
from .forms import CustomUserCreationForm
from .signals import send_email
from rest_framework import generics
from .serializers import SignUpSerializer
from rest_framework.parsers import MultiPartParser

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        send_email.send(sender=User, instance=self.object, created=True)
        return response

class SignUpAPIView(generics.CreateAPIView):
    serializer_class = SignUpSerializer
    parser_classes = [MultiPartParser]

