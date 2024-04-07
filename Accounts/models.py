from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    profile_photo = models.ImageField(verbose_name='Profile',null=True)
    #uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    
