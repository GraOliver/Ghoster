from django.contrib import admin
from .models import Produit,Boutique,CatalogBoutique,CatalogProduit
# Register your models here.
admin.site.register(Produit)
admin.site.register(CatalogProduit)