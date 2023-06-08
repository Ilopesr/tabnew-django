from django.urls import path
from apps.posts import views

urlpatterns = [
    path('comentar/post_slug/', views.add_coment, name="add_coment"),
    path('curtir/<int:pk>/', views.like, name="like"),
    path('descurtir/<int:pk>/', views.deslike, name="deslike")

]
