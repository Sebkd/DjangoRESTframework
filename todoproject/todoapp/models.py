import datetime

import django.utils.timezone
from django.db import models
from uuid import uuid4

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
    todotext = models.TextField(blank=True)
    created = models.DateTimeField(auto_created=True)
    change = models.DateTimeField(auto_now=True)
    author = models.OneToOneField(Author, on_delete=models.PROTECT)  # даже при удалении автора заметка останется
    is_active = models.BooleanField(default=True)
