from django.shortcuts import render,redirect
from django.views.generic import View


templates ="Articles/index.html"
def index(request):
    return render(request,templates)
    
