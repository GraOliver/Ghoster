from django.urls import path
from . import views


app_name="Articles"
urlpatterns=[
    path("",views.index,name="index"),
    path("Ma boutique",views.UploadPhotoVente.as_view(),name="Photo_vente"),
    path("Blog",views.Blog.as_view(),name="Blog_")
]
