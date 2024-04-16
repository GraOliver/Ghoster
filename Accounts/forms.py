from django.contrib.auth import forms,get_user_model
from django import forms as form_princ
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,UserChangeForm


class LoginUser(form_princ.Form):
    username =form_princ.CharField(max_length=63,label="Nom d'utilisateur")
    password=form_princ.CharField(max_length=63,widget=form_princ.PasswordInput,label="Mot de passe")
    pass

class UserCreationSign(UserCreationForm):
    class Meta(UserCreationForm):
        model=get_user_model()
        fields=['username','email','first_name','last_name']

class UserChangeSign(UserChangeForm):
    class Meta(UserChangeForm):
        model=get_user_model()
        fields=['username','email','first_name','last_name']
        
class UploaderPhotoUserForm(form_princ.ModelForm):
    class Meta:
        model =get_user_model()
        fields = ('profile_photo', )

 