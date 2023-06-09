from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    email = models.EmailField(max_length=255, unique=True, blank=False, null=False)
    tab_coins = models.IntegerField(blank=True,default=0)
    tab_cash = models.IntegerField(blank=True,default=0)
    email_notify = models.BooleanField("Notificação por email", default=True)

    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.username
        return super().save(*args, **kwargs)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]


    def __str__(self):
        return self.email
