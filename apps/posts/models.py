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
    comments = models.ForeignKey(
        'self', on_delete=models.CASCADE, blank=True, null=True, related_name="child_comments")
    post_date = models.DateTimeField(auto_now_add=True)
    post_edited_date = models.DateTimeField(auto_now=True)
    tab_coins = models.IntegerField(default=0, blank=False, null=False)
    slug = models.SlugField(blank=True)

    def get_total_comments(self):
        def count_comments(comment):
            count = 0  # Inicializa a contagem como zero

            # Percorre os comentários filhos aninhados
            for child_comment in comment.child_comments.all():
                count += count_comments(child_comment)

            return count + 1  # Retorna a contagem dos comentários filhos + 1

        # Começa a contagem de comentários a partir dos comentários filhos
        total_comments = count_comments(self) - 1

        return total_comments

    def save(self, *args, **kwargs):
        if not self.title:
            self.slug = slugify(f"{uuid.uuid4().hex}")
            self.title = self.slug
        elif slugify(self.title) != self.slug:
            self.slug = slugify(self.title)
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
