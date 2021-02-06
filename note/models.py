from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils import timezone


class BlogArticles(models.Model):
    title = models.CharField(max_length=300)
    # models.ForeignKey 设置外键
    author = models.ForeignKey(User, related_name="blog_post", on_delete=models.CASCADE, )
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ("-publish",)

    def __str__(self):
        return self.title
