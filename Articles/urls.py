from django.urls import path
from . import views
import math

app_name="Articles"
urlpatterns=[
    path("",views.BlogView.as_view(),name="index"),
    path("Ma vente",views.UploadPhotoVenteView.as_view(),name="vendre"),
    path("Profil_seller",views.ProfilSeller.as_view(), name="profil_seller"),
    path("Boutique_gestionnaire", views.BoutiqueGestionView.as_view(), name="boutique_creation"),
    
    
    #Bon ici nous allons juste
    path("/gestion de produit/<int:produit_id>/<int:id_boutique>/", views.DescriptionProductView.as_view(), name="produit"),
    path('/Boutique/',views.BoutiqueDescrptionView.as_view(),name='boutique_description'),# Description des tout les articles que nous avons
    
]

