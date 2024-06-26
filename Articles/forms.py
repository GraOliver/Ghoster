from django import forms
from . import models

class PhotoForm(forms.ModelForm):
    class Meta:
        model =models.Photo
        fields =['image','caption']
    


class Blog(forms.ModelForm):
    class Meta :
        model =models.Blog
        fields =['title','content']
        pass
    
    pass

class BoutiqueManegerForm(forms.ModelForm):
    class Meta:
        model =models.Boutique
        fields = ['nom_boutique','cathegorie','adresse','telephone','ville','pays','description']