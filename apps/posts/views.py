
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (CreateView,
                                  DetailView,
                                  FormView,
                                  UpdateView,
                                  DeleteView
                                  )
from django.urls import reverse, resolve, reverse_lazy


from apps.posts.models import Post
from apps.posts.forms import NewPostForm, NewCommentForm, PostUpdateForm, CommentUpdateForm
from apps.accounts.models import Account


from tabnews.utils.rule import add_point, give_like
from tabnews.utils.rule import HTTPResponseHXRedirect


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
    context = Post.objects.all()

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


@add_point
def add_coment(request, *args, **kwargs):
    if request.method == 'POST':
        description = request.POST['description']
        comment_id = request.POST['comment_id']
        object_id = request.POST['object_id']
        post_query = get_object_or_404(Post, id=object_id)
        if comment_id == '' and object_id:
            post = Post.objects.create(
                description=description,
                user=request.user,
                comments=post_query
            )
            post.save()
            return redirect('post_detail', user_slug=post_query.user.slug, post_slug=post_query.slug)
        else:
            comment_query = get_object_or_404(Post, id=comment_id)
            post = Post.objects.create(
                description=description,
                user=request.user,
                comments=comment_query
            )
            post.save()
            return redirect('post_detail', user_slug=post_query.user.slug, post_slug=post_query.slug)
    return redirect('index')


def like(request, pk, *args, **kwargs):

    try:
        user = Account.objects.get(email=request.user.email)
        if user.tab_coins <= 1:
            return HTTPResponseHXRedirect(request.META.get('HTTP_REFERER'))
        else:
            id = request.POST[f'id-{pk}']
            post_query = get_object_or_404(Post, id=id)
            post_query.tab_coins += 1
            post_query.save()
            user.tab_cash += 1
            user.tab_coins -= 2
            user.save()
    except ValueError:
        pass

    return HTTPResponseHXRedirect(request.META.get('HTTP_REFERER'))


def deslike(request, pk, *args, **kwargs):
    try:
        user = Account.objects.get(email=request.user.email)
        if user.tab_coins <= 1:
            return HTTPResponseHXRedirect(request.META.get('HTTP_REFERER'))
        else:
            id = request.POST[f'id-{pk}']
            post_query = get_object_or_404(Post, id=id)
            post_query.tab_coins -= 1
            post_query.save()
            user.tab_coins -= 2
            user.save()
    except ValueError:
        pass
    return HTTPResponseHXRedirect(request.META.get('HTTP_REFERER'))


class PostUpdateView(UpdateView):
    template_name = "pages/posts/edit_post.html"
    model = Post
    form_class = PostUpdateForm

    def get_object(self):
        slug = self.kwargs.get('post_slug')
        return get_object_or_404(Post, slug=slug)

    def form_valid(self, form):
        user = Account.objects.get(email=self.request.user.email)
        user_form = form.save(commit=False)
        user_form.user = user
        user_form.save()
        return super().form_valid(form)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(PostUpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['instance'] = Post.objects.get(
            slug=self.kwargs.get('post_slug'))
        return kwargs


class PostDeleteView(DeleteView):
    template_name = "pages/posts/post_detail.html"
    model = Post

    def get_object(self):
        slug = self.kwargs.get('post_slug')
        return get_object_or_404(Post, slug=slug)

    def post(self, request, *args, **kwargs):
        uri = self.request.META.get('HTTP_REFERER')
        uri_parts = uri.split('/')
        uri_parts_sep = list(filter(str.strip, uri_parts))
        user_slug = uri_parts_sep[-2]
        post_slug = uri_parts_sep[-1]
        slug = self.kwargs.get('post_slug')
        post = get_object_or_404(Post, slug=slug)
        post.delete()
        if post.comments is not None:
            return HTTPResponseHXRedirect(redirect_to=reverse_lazy('post_detail', kwargs={'user_slug': user_slug, 'post_slug': post_slug}))
        else:
            return HTTPResponseHXRedirect(redirect_to=reverse_lazy(('index')))


class CommentUpdateView(UpdateView):
    template_name = "pages/posts/edit_comment.html"
    model = Post
    form_class = CommentUpdateForm

    def get_object(self):
        slug = self.kwargs.get('post_slug')
        return get_object_or_404(Post, slug=slug)

    def get_success_url(self):
        super().get_success_url()
        # Obtenha o referer HTTP
        referer = self.request.META.get('HTTP_REFERER')
        uri_parts = referer.split('/')
        uri_parts_sep = list(filter(str.strip, uri_parts))
        user_slug = uri_parts_sep[-2]
        post_slug = uri_parts_sep[-1]
        return HttpResponseRedirect(redirect_to=reverse_lazy('post_detail', kwargs={'user_slug': user_slug, 'post_slug': post_slug}))

    def form_valid(self, form):
        user = Account.objects.get(email=self.request.user.email)
        user_form = form.save(commit=False)
        user_form.user = user
        user_form.save()
        return self.get_success_url()

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CommentUpdateView, self).get_form_kwargs(
            *args, **kwargs)
        kwargs['instance'] = Post.objects.get(
            slug=self.kwargs.get('post_slug'))
        return kwargs
