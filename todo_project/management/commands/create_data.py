from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group, Permission
from authors.models import Author, Book
from todoapp.models import Project, ToDo


class Command(BaseCommand):

    def handle(self, *args, **options):
        Book.objects.all().delete()
        ToDo.objects.all().delete()
        Project.objects.all().delete()
        Author.objects.all().delete()
        User.objects.all().delete()

    #