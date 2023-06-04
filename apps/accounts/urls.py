from django.urls import path
from apps.accounts import views
urlpatterns = [
    path('', views.AccountView.as_view(), name="account"),
]