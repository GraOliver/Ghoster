from django.contrib import admin
from .models import Produit,Boutique,CatalogBoutique,CatalogProduit,CarouselPhotoDescription,Panier,Order
# Register your models here.
admin.site.register(Produit)
admin.site.register(CatalogProduit)
admin.site.register(CatalogBoutique)
admin.site.register(Boutique)
admin.site.register(CarouselPhotoDescription)
admin.site.register(Order)
admin.site.register(Panier)