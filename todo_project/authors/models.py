from uuid import uuid4

from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User
from rest_framework import serializers


class Author(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid4)
    username = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    # username = models.OneToOneField(User, on_delete=models.CASCADE)
    # username = models.CharField(max_length=64)
    # first_name = models.CharField(max_length=64)
    # first_name = models.CharField(U)
    # last_name = models.CharField(max_length=64)
    # birthday_year = models.PositiveIntegerField(blank=True, default=)
    # email = models.EmailField(unique=True)

    def __str__(self):
        return self.username.username





    # def get_full_name (self):
    #     return self.first_name + ' ' + self.last_name


# class Author(models.Model):
#     uid = models.UUIDField(primary_key=True, default=uuid4)
#     username = models.CharField(max_length=64)
#     first_name = models.CharField(max_length=64)
#     last_name = models.CharField(max_length=64)
#     birthday_year = models.PositiveIntegerField()
#     email = models.EmailField(unique=True)
#
#     def __str__(self):
#         # return self.first_name + ' ' + self.last_name
#         return self.username


class Biography(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid4)
    text = models.TextField()
    author = models.OneToOneField(Author, on_delete=models.CASCADE)


class Book(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=32)
    authors = models.ManyToManyField(Author)


class Article(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=32)
    author = models.ForeignKey(Author, models.PROTECT)
