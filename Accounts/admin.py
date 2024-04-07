from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import UserCreationSign,UserChangeSign

admin.site.register(User,UserAdmin)
class UserAdmin(UserAdmin):
    add_form=UserCreationSign
    form=UserChangeSign
    model=User
    