from django.urls import path
from apps.accounts import views
urlpatterns = [
    path('sair/', views.LogoutView.as_view(), name="logout"),
    path('perfil/', views.AccountView.as_view(), name="account"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('cadastrar/', views.NewAccountView.as_view(), name="signup"),
    path('cadastrar/<uidb64>/<token>/', views.new_account_active, name="signup_active"),
    path('cadastro/recuperar/', views.RecoverPasswordView.as_view(), name="recover"),
    path('cadastro/recuperar/confirmar/',
         views.NotifyEmailView.as_view(), name="email_notify"),
    path('cadastro/recuperar/senha/decode/<uidb64>/<token>/',
         views.recover_password_decode, name="recover_decode"),
    path('cadastro/recuperar/senha/validado/',
         views.ChangePasswordView.as_view(), name="change_password"),
]