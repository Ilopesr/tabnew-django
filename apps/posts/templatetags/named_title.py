from django import template

register = template.Library()

from apps.posts.models import Post
from django.shortcuts import get_object_or_404

@register.filter
def title_name(path):
    try:
        r_path = list(filter(bool, path.split("/")))
        verify = lambda name_list: [ i in r_path for i in name_list]
        if all(verify(["cadastro","recuperar","perfil"])):
            return "Editar perfil · "
        else:
            queryset = Post.objects.get(slug=r_path[1])
            return f"{queryset.title} · "
    except:
        return ""