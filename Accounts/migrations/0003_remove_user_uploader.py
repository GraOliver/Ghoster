# Generated by Django 3.2.23 on 2024-04-07 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0002_alter_user_profile_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='uploader',
        ),
    ]
