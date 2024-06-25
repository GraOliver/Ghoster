from django.urls import path
from . import views


app_name="Articles"
urlpatterns=[
    path("",views.index,name="index"),
    path("Ma boutique",views.UploadPhotoVenteView.as_view(),name="Boutique"),
    path("./Profil_seller",views.ProfilSeller.as_view(), name="profil_seller"),
    path("Blog",views.Blog.as_view(),name="Blog_")
]
