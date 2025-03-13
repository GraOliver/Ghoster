from django.db import models
from django.conf import settings


class Photo(models.Model):
    """La classe qui vas gerer les photos de notre app
    """
    image = models.ImageField()
    caption = models.CharField(max_length=128, blank=True)
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.caption
    
class CatalogProduit(models.Model):
    cathegorie =models.CharField(max_length =150)
    def __str__(self):
        return self.cathegorie
class CatalogBoutique(models.Model):
    cathegorie =models.CharField(max_length =150)
    def __str__(self):
        return self.cathegorie
    
class Blog(models.Model):
    
    photo = models.ForeignKey(Photo, null=True, on_delete=models.SET_NULL, blank=True)
    title = models.CharField(max_length=128)
    content = models.TextField(max_length=5000)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    starred = models.BooleanField(default=False)
    def __str__(self):
        return self.title

class Boutique(models.Model):
    #indetity of boutique
    photo = models.ForeignKey(Photo, null=True, on_delete=models.SET_NULL, blank=True)
    nom_boutique = models.CharField(max_length=128,verbose_name='Nom de la boutique')
    cathegorie =models.ForeignKey(CatalogBoutique,on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    #localisation de la boutique et telephone
    adresse=models.CharField(max_length=150)
    telephone=models.CharField(max_length=14)
    ville=models.CharField(max_length=155)
    pays =models.CharField(max_length=155)
    #Us=tilisateur
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #information supplementaire
    description = models.TextField(max_length=500)
    starred = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nom_boutique

class Produit(models.Model):
    
    #information sur le produit
    libele=models.CharField(max_length=120)
    quantite =models.IntegerField(max_length=50)
    prix=models.FloatField(max_length=50)
    cathegorie =models.ForeignKey(CatalogProduit,on_delete=models.CASCADE)
    description=models.TextField(max_length=200)
    photo = models.ForeignKey(Photo, null=True, on_delete=models.SET_NULL, blank=True)
    
    #identite du vendeur
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    boutique =models.ForeignKey(Boutique,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.libele

class CarouselPhotoDescription(models.Model):
    titre =models.CharField(max_length=25)
    description=models.CharField(max_length=50)
    photo =models.ForeignKey(Photo,null=False,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.titre