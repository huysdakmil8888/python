from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .celery import app
from django.core.mail import send_mail
from accounts.models import User
from django.contrib.auth import get_user_model
from datetime import datetime, timedelta
from django.db import connections


User = get_user_model()
import logging
logger = logging.getLogger(__name__)
logging.basicConfig(filename='app.log', level=logging.INFO)


@shared_task
def send_confirmation_email(user_id):
    print('ok22')
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        print(f'User with id {user_id} does not exist.')
        return
    send_mail(
        'Thank you for signing up.',  # subject
        'welcome to our website',  # message
        'huy@example.com',  # from email
        [user.email],  # to email
        fail_silently = False # to log error , if smtp send fail

    )

@app.task
def send_daily_signup_email():
    logger.info('Running send_daily_signup_email task')
    print('loop')
    one_day_ago = datetime.now() - timedelta(days=1)
    new_users = User.objects.filter(date_joined__gte=one_day_ago)
    email_body = 'Here are the users who signed up today:\n\n'
    for user in new_users:
        email_body += f'- {user.username} ({user.email})\n'

    send_mail(
        'Daily new user signup',
        email_body,
        'from@example.com',
        ['receiver@example.com'],
        fail_silently=False,
    )

@app.task
def db_health_check():
    db_conn = connections['default']
    try:
        db_conn.cursor()
        # raise Exception('Test exception') , force exception
    except Exception as e:
        print('exception')
        send_mail(
            'DB Health Check Failed',
            f'The DB health check failed with the following error:\n\n{e}',
            'from@example.com',
            ['admin@example.com'],
            fail_silently=False,
        )