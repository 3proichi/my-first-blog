from django.conf import settings
from django.db import models
from django.utils import timezone
from django import forms


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(verbose_name="タスク名",blank=False, null=False, max_length=10, default=" ")
    text = models.TextField(verbose_name="タスク内容")
    deadline = models.DateTimeField(verbose_name="締切日時", blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title