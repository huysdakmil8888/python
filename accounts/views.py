# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.core.mail import send_mail
from accounts.models import User
from .forms import CustomUserCreationForm
from .signals import send_email


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        send_email.send(sender=User, instance=self.object, created=True)
        return response


class loginView(CreateView):
    # form_class = CustomUserCreationForm
    # success_url = reverse_lazy("login")
    template_name = "registration/login.html"