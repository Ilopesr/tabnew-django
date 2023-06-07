from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, DetailView, FormView
from django.urls import reverse, resolve


from apps.posts.models import Post
from apps.posts.forms import NewPostForm, NewCommentForm
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


class PostDetailView(DetailView, FormView):
    template_name = "pages/posts/post_detail.html"
    model = Post
    form_class = NewCommentForm

    def get(self, *args, **kwargs):
        try:
            user_slug = self.kwargs.get('user_slug')
            post_slug = self.kwargs.get('post_slug')

            queryset = get_object_or_404(
                Post, user__slug=user_slug, slug=post_slug)

            context = {
                'object': queryset,
                'form': NewCommentForm()
            }
            return render(self.request, self.template_name, context)
        except ValueError:
            pass


def add_coment(request, *args, **kwargs):
    if request.method == 'POST':
        description = request.POST['description']
        comment_id = request.POST['comment_id']

        if comment_id == '':

            post = Post.objects.create(
                description=description,
                user=request.user,
            )
        else:
            post_obj = get_object_or_404(Post, comments=comment_id)
            post = Post.objects.create(
                description=description,
                user=request.user,
                comments=post_obj,
            )
            post.

    return redirect('index')
