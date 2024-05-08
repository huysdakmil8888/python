from django.dispatch import receiver,Signal
from app.tasks import send_confirmation_email


# custom signals
# send_email = Signal()

# @receiver(send_email, sender=User)
# def send_welcome_email(sender, instance, created, **kwargs):
#     send_mail(
#         'Welcome to our website',  # subject
#         'Thank you for signing up.',  # message
#         'from@example.com',  # from email
#         [instance.email],  # to email
#     )


user_signed_up = Signal()

@receiver(user_signed_up)
def handle_user_signed_up(sender, user_id, **kwargs):
    send_confirmation_email.delay(user_id)