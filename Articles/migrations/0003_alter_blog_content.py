# Generated by Django 5.0.4 on 2024-05-06 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0002_catalog_remove_photo_caption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.TextField(max_length=5000),
        ),
    ]
