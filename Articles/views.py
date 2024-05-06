from django.shortcuts import render,redirect
from django.views.generic import View
from django.template import loader
from django.contrib.auth.decorators import login_required
from . import models,forms

templates ="Articles/base.html"
def index(request):
    actualite={
        "actualite" :models.Blog.objects,
               }
    return render(request,templates)
    
class UploadPhotoVenteView(View):
    template = "Articles/boutique.html"
    get_photo =forms.PhotoForm
    get_blog =forms.Blog
    
    # gestion des utillisateur connecter
    def get(self,request):
        form={
            "photo_form" : self.get_photo(),
            "blog_form" : self.get_blog()
        }
        return render(request,self.template,form)
        
            
    #@login_required # gestion des utillisateur connecter
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
            
            
    pass

class Blog(View):
    def get(self,request):
        pass
    def post(self,request):
        pass
    pass
