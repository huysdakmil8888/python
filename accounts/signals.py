import django.core.mail
from django.db.models.signals import post_save
from django.dispatch import receiver,Signal
from .models import User
from django.core.mail import send_mail


# custom signals
send_email = Signal()

@receiver(send_email, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    send_mail(
        'Welcome to our website',  # subject
        'Thank you for signing up.',  # message
        'from@example.com',  # from email
        [instance.email],  # to email
    )