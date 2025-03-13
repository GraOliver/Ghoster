from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import View
from django.template import loader
from django.contrib.auth.decorators import login_required
from . import models,forms
from .models import Blog,Boutique,Produit,CarouselPhotoDescription
import random
from django.core.paginator import Paginator


class BlogView(View):
    template="Articles/index.html"
    list_produit_hasard =[]
    try :
        list_produit_hasard =Produit.objects.get(pk=random.randint(0,100))
        pass
    except Produit.DoesNotExist :
        list_produit_hasard =get_object_or_404(Produit,pk=1)   
        pass  
    
    contents ={
        'article':Produit.objects.all(), 
        'produit_principal_hasard' :get_object_or_404(Produit,pk=1),
        'produit_carousel':CarouselPhotoDescription.objects.all()
    }
    
    def get (self,request):
        return render(request,self.template,self.contents)
    
class UploadPhotoVenteView(View):
    template = "Articles/boutique/boutique.html"
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
    template ="Articles/boutique/boutique_manage.html"
    get_photo =forms.PhotoForm
    get_boutique =forms.BoutiqueManegerForm
    
    #@login_required    
    def get (self,request):
        context ={
            "boutique_form":self.get_boutique(),
            "photo_form":self.get_photo()
        }
        return render(request,self.template,context)
    def post(self,request):
       boutique_form=self.get_boutique(request.POST)
       photo_form =self.get_photo(request.POST,request.FILES)
       if all([boutique_form.is_valid(),photo_form.is_valid()]):
           #organisation de la photo
           photo=photo_form.save(commit=False)
           photo.uploader=request.user
           photo.save()
           
           boutique =boutique_form.save(commit=False)
           boutique.author =request.user
           boutique.photo =photo
           boutique.save()
           return redirect("Articles:index")
       else :
           return render(request,self.template)

class BoutiqueDescrptionView(View):
     templetes ="Articles/boutique/boutique.html"
    #  @login_required
     def get(self,request):
         context ={
             'response' :Boutique.objects.all()
         }
         
         return render(request,self.templetes,context)
                   
class ProduitView(View):
    templetes ="Articles/articles/description_articles.html"
    produits =Produit.objects.all
    pagination =Paginator(produits, 5)
    pagination_bando =Paginator(produits,4)
    def get(self,request):
        context ={
            "produit ":self.produits,
            "pagination" :self.pagination.get_page(request.get('page')),
            "bando_pagination" :self.pagination_bando.get_page(request.get('bando_page'))
        }
        return render(request,self.templetes,context)
    def post(self,request):
        pass
    
class ProfilSeller(View):
    templates='articles/user/description_compte.html'
    def get(self,request):
        return render(request,self.templates)
    def post(self,request):
        pass
    
class DescriptionProductView(View):
    template ="Articles/boutique/communication.html"
    def get(self,request,produit_id):
        context ={'description_prosuit':get_object_or_404(Produit,pk = produit_id)}
        return render(request,self.template,context)
       
        