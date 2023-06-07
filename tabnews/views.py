from django.views.generic import TemplateView
from apps.posts.models import Post

from django.db.models import Count, Case, When, F
from django.db import models


class IndexView(TemplateView):
    template_name = "pages/home/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.exclude(comments__isnull=False)
        return context
