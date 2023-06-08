from django.urls import path
from apps.posts import views

urlpatterns = [
    path('posts/comentar/post_slug/', views.add_coment, name="add_coment"),
    path('posts/curtir/<int:pk>/', views.like, name="like"),
    path('posts/descurtir/<int:pk>/', views.deslike, name="deslike"),
    path('publicar/', views.NewPostView.as_view(), name="new_post"),
    path('<slug:user_slug>/<slug:post_slug>/',
         views.PostDetailView.as_view(), name="post_detail"),

]
