from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField()
    coments = models.ManyToManyField('Comment')


class Comment(models.Model):
    pass

