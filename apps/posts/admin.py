from django.contrib import admin
from apps.posts.models import Post


@admin.register(Post)
class PostModel(admin.ModelAdmin):
    list_display = ['id', 'title', 'tab_coins',
                    'source', 'post_date', 'post_edited_date']
