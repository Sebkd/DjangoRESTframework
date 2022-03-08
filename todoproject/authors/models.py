from uuid import uuid4

from django.db import models

class Author(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid4)
    username = models.CharField(max_length=64)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthday_year = models.PositiveIntegerField()
    email = models.EmailField(unique=True)

class Biography(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid4)
    text = models.TextField()
    author = models.OneToOneField(Author, on_delete=models.CASCADE)

class Book(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=32)
    author = models.ManyToManyField(Author)

class Article(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=32)
    author = models.ForeignKey(Author, models.PROTECT)




# Create your models here.
