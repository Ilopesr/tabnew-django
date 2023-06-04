from django.views.generic import TemplateView
from apps.posts.models import Post
class IndexView(TemplateView):
    template_name = "pages/home/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context
