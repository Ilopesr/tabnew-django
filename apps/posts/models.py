from markdownx.models import MarkdownxField

from django.urls import reverse
from django.db import models
from django.utils.text import slugify


from apps.accounts.models import Account

class Post(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False, null=False)
    description = MarkdownxField()
    source = models.URLField(blank=True)
    coments = models.ManyToManyField('Comment',blank=True)
    post_date = models.DateField(auto_now_add=True)
    post_edited_date = models.DateField(auto_now=True)
    tab_coins = models.IntegerField(default=0, blank=False, null=False)

    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


    def get_absolute_url(self, *args, **kwargs):
        return reverse('index')

    def __str__(self):
        return self.title

class Comment(models.Model):
    pass

