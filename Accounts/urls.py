from django.urls import path
from . import views
from django.contrib.auth import views as vue # importation de la bubliothèque pour la reunitialisation de
app_name="Accounts"
urlpatterns=[
    path("",views.LoginUserView.as_view(),name="login_user"),
    path("register/",views.UserCreationView.as_view(),name="register_user"),
    path("User_change/",views.UserChangeView.as_view(),name="change_user"),
    path("logout_user/",views.UserLogoutView.as_view(),name="logout_user"),
    path("password_change/",vue.PasswordChangeView.as_view(),name="password"),
    path("User_change_profil/",views.upload_profile_photo,name="change_profil"),
    
    # nous chargeons les urls pour la reunitialisation du mot de passe
    path("reset_password", vue.PasswordResetView.as_view(),name="pass_forgeted" ),
    path("reset_password_send",vue.PasswordResetDoneView.as_view(),name="password_reset_done"),
    path("reset/<uidb64>/<token>",vue.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path("reset_password_complete",vue.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
]