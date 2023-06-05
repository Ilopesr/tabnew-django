from django.shortcuts import render, redirect
from django.views.generic import CreateView,DetailView,TemplateView
from django.urls import reverse
from apps.posts.models import  Post
from apps.posts.forms import NewPostForm
from apps.accounts.models import Account

class NewPostView(CreateView):
    template_name = "pages/posts/new_post.html"
    model = Post
    form_class = NewPostForm
    success_url = "/"  # ou use a função reverse_lazy para obter a URL dinamicamente

    def form_valid(self, form):
        user = Account.objects.get(email=self.request.user.email)
        user_form = form.save(commit=False)
        user_form.user = user
        user_form.save()
        return super().form_valid(form)


class PostDetailView(TemplateView):
    template_name = "pages/posts/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = Post.objects.get(slug=kwargs.get('post_slug'))

        return context



