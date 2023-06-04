from django.urls import path
from apps.accounts import views
urlpatterns = [
    path('', views.AccountView.as_view(), name="account"),
    path('recuperar/', views.RecoverPasswordView.as_view(), name="recover"),
    path('recuperar/confirmar/', views.NotifyEmailView.as_view(), name="email_notify"),
    path('recuperar/senha/decode/<uidb64>/<token>/', views.recover_password_decode, name="recover_decode"),
    path('recuperar/senha/validado/', views.ChangePasswordView.as_view(), name="change_password"),
]