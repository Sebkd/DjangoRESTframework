import datetime

import django.utils.timezone
from django.db import models
from uuid import uuid4

from django.utils import timezone

from authors.models import Author


class Project(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=128)
    link = models.URLField(blank=True)
    authors = models.ManyToManyField(
        Author)  # один автор может иметь несколько проектов и проект может иметь несколько авторов

    def __str__(self):
        return self.name


class ToDo(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid4)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)  # жестко привязываем к проекту
    content = models.TextField(blank=True)
    is_created = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # дата создания
    is_change = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)  # даже при удалении автора заметка останется
    is_active = models.BooleanField(default=True, auto_created=True)
