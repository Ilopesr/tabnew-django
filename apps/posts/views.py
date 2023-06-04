from django.shortcuts import render
from django.views.generic import CreateView,DetailView,TemplateView
from django.urls import reverse
from apps.posts.models import  Post

class NewPostView(CreateView):
    template_name = "pages/posts/new_post.html"
    model = Post
    fields = ['title','description','source']

class PostDetailView(TemplateView):
    template_name = "pages/posts/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = Post.objects.get(title=kwargs.get('post_slug'))

        return context



