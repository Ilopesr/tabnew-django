from django.shortcuts import render, redirect, get_object_or_404
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


class PostDetailView(DetailView):
    template_name = "pages/posts/post_detail.html"
    model = Post

    def get(self, *args, **kwargs):
        try:
            user_slug = self.kwargs.get('user_slug')
            post_slug = self.kwargs.get('post_slug')
            queryset = get_object_or_404(Post, user__slug=user_slug, slug=post_slug)
            context = {
                'object': queryset
            }
            return render(self.request, self.template_name, context)
        except ValueError:
            pass





