from django import forms
from . import models

class PhotoForm(forms.ModelForm):
    class Meta:
        model =models.Photo
        fields =['image','caption']
    
    pass

class Blog(forms.ModelForm):
    class Meta :
        model =models.Blog
        fields =['title','content']
        
