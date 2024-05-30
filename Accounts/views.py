from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserChangeSign,LoginUser,UserCreationSign,UploaderPhotoUserForm
from django.contrib.auth import login,logout,authenticate
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from . import models

class LoginUserView(View):
    """Cette classe permet de verifier la connexion 

    Args:
        View (_type_): _description_
    
    """
    message_error ="Mot de passe ou mon d'utilisatuer inconnue"
    templates ="Accounts/login.html"
    class_form_login =LoginUser
    
    def get(self,request):
        form = LoginUser()   
        return render(request,self.templates,{'form':form})
    
    def post(self,request):
        form = self.class_form_login(request.POST)
        if form.is_valid():
            user =authenticate(
                request,
                username =form.cleaned_data["username"],
                password =form.cleaned_data["password"]
            )
            
            if user is not None :
                login(request,user)
                return redirect('Articles:index')
            else :
                messages.info(request,self.message_error)
                pass
            pass

        return render(request,self.templates,{"form":form})

class UserLogoutView(View):
    def get(self,request ):
        logout(request)
        return redirect("Accounts:login_user")

class UserCreationView(View):
    """Cette fonction est pour la création d'un nouveau utilisateur

    Args:
        View (_type_): _description_

    Returns:
        _type_: _description_
    """
    class_get_element =UserCreationSign
    templates ="Accounts/register.html"
    
    def get(self,request):
        form =self.class_get_element()
        return render(request,self.templates,{"form":form})
    
    def post(self,request):
        form =self.class_get_element(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect("Accounts:change_profil")
        
        return render(request,self.templates,{"form":form})

class UserChangeView(View):
    form_class =UserChangeSign
    templates ="Accounts/change.html"
    
    
    def get(self,request):
        form =self.form_class()
        #getion de l'image du profil
        context ={
            "form":form,
            "image_profile":models.User.objects.all()
        }
        return render(request,self.templates,context)
    
    def post(self,request):
        form =self.form_class(request.POST)
        context ={
            "form":form,
        }

        if form.is_valid():
            form.changed_data
            return redirect("Articles:index")
        
        return render(request,self.templates,context)
    pass

class UploadProfilUserView(View):
    templates ="Accounts/profile.html"
    class_photo_form=UploaderPhotoUserForm
    
    def get (self, request):
        form =UploaderPhotoUserForm()
        return render(request,self.templates,{"form":form})
            
    def post(self,request):
        form = self.class_photo_form(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("Articles:index") 
        
        return render(request,self.templates,{"form":form})          

        