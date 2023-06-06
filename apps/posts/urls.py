from django.urls import path
from apps.posts import views

urlpatterns = [
    path('comentar/<int:pk>/<post_slug>/', views.add_post, name="add_post" )
]