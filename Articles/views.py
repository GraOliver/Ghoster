from django.shortcuts import render,redirect
from django.views.generic import View
from django.template import loader
from django.contrib.auth.decorators import login_required
from . import models,forms
from .models import Blog,Boutique
import random
templates ="Articles/index.html"
def index(request):
    contexts ={
        'Article':models.Blog.objects.all()
    }
    return render(request,templates,contexts)

class Blog(View):
    template="Articles/index"
    contents ={
        'Article':Blog.objects.all()
    }
    def get (self,request):
        return render(request,self.template,self.contents)
    
class UploadPhotoVenteView(View):
    template = "Articles/boutique.html"
    get_photo =forms.PhotoForm
    get_blog =forms.Blog
    
    # @login_required # gestion des utillisateur connecter
    def get(self,request):
        form={
            "photo_form" : self.get_photo(),
            "blog_form" : self.get_blog()
        }
        return render(request,self.template,form)
        
            
    # @login_required # gestion des utillisateur connecter
    def post(self,request):
        photo_form= self.get_photo(request.POST, request.FILES)
        blog_form = self.get_blog(request.POST)
        
        if all([photo_form.is_valid(),blog_form.is_valid()]):
            photo =photo_form.save(commit=False)
            photo.uploader =request.user
            photo.save()
            
            blog=blog_form.save(commit=False)
            blog.author =request.user
            blog.photo =photo
            blog.save()
            return redirect("Articles:index")
        else :
            return render(request,self.template)
        
        return redirect("Articles:index")
           
    pass

class BoutiqueGestionView(View):
    template ="Articles/boutique_manage.html"
    get_photo =forms.PhotoForm
    get_boutique =forms.BoutiqueManegerForm
        
    def get (self,request):
        context ={
            "boutique_form":self.get_boutique(),
            "photo_form":self.get_photo()
        }
        return render(request,self.template,context)
        
class ProduitView(View):
    def get(self,request):
        pass
    
class ProfilSeller(View):
    def get(self,request):
        pass
    def post(self,reauest):
        pass