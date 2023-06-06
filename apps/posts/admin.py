from django.contrib import admin
from apps.posts.models import Post, Comment

admin.site.register(Comment)
# Register your models here.

@admin.register(Post)
class PostModel(admin.ModelAdmin):
    list_display = ['id','title','tab_coins','source','post_date','post_edited_date']