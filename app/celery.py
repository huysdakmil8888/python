from __future__ import absolute_import, unicode_literals
from celery import Celery
import os
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

app = Celery('app', broker='redis://localhost:6379/0')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
app.config_from_object('django.conf:settings', namespace='CELERY')


app.conf.beat_schedule = {
    'send_daily_signup_email': {
        'task': 'app.tasks.send_daily_signup_email',
        'schedule': crontab(hour=17, minute=21),
    },
    'db_health_check': {
        'task': 'app.tasks.db_health_check',
        'schedule': crontab(),
    },
}

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
