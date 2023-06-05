from django.shortcuts import render, redirect
from django.views.generic import CreateView,DetailView,TemplateView
from django.urls import reverse
from apps.posts.models import  Post
from apps.accounts.models import Account
class NewPostView(CreateView):
    template_name = "pages/posts/new_post.html"
    model = Post
    fields = ['title','description','source']


    def form_valid(self, form):
        user = Account.objects.get(email=self.request.user.email)
        user_form = form.save(commit=False)
        user_form.user = user
        user_form.save()
        return redirect('index')


class PostDetailView(TemplateView):
    template_name = "pages/posts/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = Post.objects.get(slug=kwargs.get('post_slug'))

        return context



