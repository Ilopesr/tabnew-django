import datetime
import pytz
import uuid

from markdownx.models import MarkdownxField

from django.conf import settings
from django.urls import reverse
from django.db import models
from django.utils.text import slugify


from apps.accounts.models import Account

class Post(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False, null=False)
    description = MarkdownxField()
    source = models.URLField(blank=True)
    comments = models.ManyToManyField('Comment',blank=True, related_name="comments")
    post_date = models.DateTimeField(auto_now_add=True)
    post_edited_date = models.DateTimeField(auto_now=True)
    tab_coins = models.IntegerField(default=0, blank=False, null=False)

    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        else:
            if self.slug != self.title:
                self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    import datetime

    def post_at(self):
        try:
            sao_paulo_tz = pytz.timezone(settings.TIME_ZONE)
            current_datetime = datetime.datetime.now(sao_paulo_tz)  # Get the current datetime in the Sao Paulo timezone
            post_datetime = self.post_date.replace(
                tzinfo=sao_paulo_tz)  # Make the post datetime timezone-aware in Sao Paulo timezone
            data = current_datetime - post_datetime

            if data.days == 0:
                hours = data.seconds // 3600
                if hours == 0:
                    return "Agora mesmo"
                elif hours == 1:
                    return f"{hours} hora atrás"
                else:
                    return f"{hours} horas atrás"
            elif data.days == 1:
                return "1 dia atrás"
            else:
                return f"{data.days} dias atrás"
        except:
            pass

    def get_absolute_url(self, *args, **kwargs):
        return reverse('index')



    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    description = MarkdownxField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='post_comments', blank=True, null=True)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='child_comments')
    post_date = models.DateTimeField(auto_now_add=True)
    post_edited_date = models.DateTimeField(auto_now=True)
    tab_coins = models.IntegerField(default=0, blank=False, null=False)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.description

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{uuid.uuid4().hex}")
        return super().save(*args, **kwargs)

    import datetime

    def post_at(self):
        try:
            sao_paulo_tz = pytz.timezone(settings.TIME_ZONE)
            current_datetime = datetime.datetime.now(sao_paulo_tz)  # Get the current datetime in the Sao Paulo timezone
            post_datetime = self.post_date.replace(
                tzinfo=sao_paulo_tz)  # Make the post datetime timezone-aware in Sao Paulo timezone
            data = current_datetime - post_datetime

            if data.days == 0:
                hours = data.seconds // 3600
                if hours == 0:
                    return "Agora mesmo"
                elif hours == 1:
                    return f"{hours} hora atrás"
                else:
                    return f"{hours} horas atrás"
            elif data.days == 1:
                return "1 dia atrás"
            else:
                return f"{data.days} dias atrás"
        except:
            pass

    def get_absolute_url(self, *args, **kwargs):
        return reverse('index')

