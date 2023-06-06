import datetime
import pytz
import uuid

from markdownx.models import MarkdownxField

from django.db import models

from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify


from apps.accounts.models import Account


class Post(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True, null=False)
    description = MarkdownxField()
    source = models.URLField(blank=True)
    comments = models.ManyToManyField(
        'self', blank=True, related_name="child_comments", symmetrical=False)
    post_date = models.DateTimeField(auto_now_add=True)
    post_edited_date = models.DateTimeField(auto_now=True)
    tab_coins = models.IntegerField(default=0, blank=False, null=False)

    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        if not self.title:
            self.slug = slugify(f"{uuid.uuid4().hex}")
        else:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def post_at(self):
        sao_paulo_tz = pytz.timezone(settings.TIME_ZONE)
        # Get the current datetime in the Sao Paulo timezone
        current_datetime = datetime.datetime.now(sao_paulo_tz)
        # Make the post datetime timezone-aware in Sao Paulo timezone
        post_datetime = self.post_date
        data = current_datetime - post_datetime
        if data.days <= 0:
            hours = data.seconds // 3600
            if hours == 0:
                return "Agora mesmo"
            elif hours == 1:
                return f"{hours} hora atrás"
            else:
                return f"{hours} horas atrás"
        elif data.days == 1:
            return "1 dia atrás"
        elif data.days > 1:

            return f"{data.days} dias atrás"
        else:
            return ""

    def get_absolute_url(self, *args, **kwargs):
        return reverse('index')

    def __str__(self):
        return self.title
