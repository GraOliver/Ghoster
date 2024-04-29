from django.shortcuts import render,redirect
from django.views.generic import View
from django.template import loader
from django.contrib.auth.decorators import login_required
from . import models,forms

templates ="Articles/base.html"
def index(request):
    return render(request,templates)
    
class UploadPhotoVente(View):
    @login_required # gestion des utillisateur connecter
    def get(self,request):
        pass
    @login_required # gestion des utillisateur connecter
    def post(self,request):
        pass
    pass

class Blog(View):
    def get(self,request):
        pass
    def post(self,request):
        pass
    pass
