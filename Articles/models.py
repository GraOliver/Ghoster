from django.db import models
from django.conf import settings


class Photo(models.Model):
    """La classe qui vas gerer les photos de notre app
    """
    image = models.ImageField()
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    
class Catalog(models.Model):
    id_catalog =models.CharField(max_length =25)
    cathegorie =models.CharField(max_length =150)
    
class Blog(models.Model):   
    photo = models.ForeignKey(Photo, null=True, on_delete=models.SET_NULL, blank=True)
    title = models.CharField(max_length=128)
    content = models.TextField(max_length=5000)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    starred = models.BooleanField(default=False)
    
