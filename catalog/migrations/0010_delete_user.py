# Generated by Django 5.0.4 on 2024-04-28 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_alter_category_image_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
