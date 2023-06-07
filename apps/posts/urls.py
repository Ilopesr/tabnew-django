from django.urls import path
from apps.posts import views

urlpatterns = [
    path('comentar/post_slug/', views.add_coment, name="add_coment")

]
