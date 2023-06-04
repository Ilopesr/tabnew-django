from django.contrib import admin
from apps.posts.models import Post, Comment
from markdownx.admin import MarkdownxModelAdmin
admin.site.register(Post,MarkdownxModelAdmin)
admin.site.register(Comment)
# Register your models here.
