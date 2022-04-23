import os
import uuid

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group, Permission
from rest_framework.utils import json

from authors.models import Author, Book
from todoapp.models import Project, ToDo

JSON_PATH = "/home/andrey/Project_Pycharm/DjangoRESTframework/todo_project/jsons/"


def load_from_json(file_nm):
    """
    """
    with open(os.path.join(JSON_PATH, file_nm + '.json'), 'r', encoding='utf-8') as ld_file:
        return json.load(ld_file)


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Book.objects.all().delete()
        # ToDo.objects.all().delete()
        # Project.objects.all().delete()
        # Author.objects.all().delete()
        # User.objects.all().delete()

        users = load_from_json('users')
        User.objects.all().delete()
        for user in users:
            new_user = User(**user)
            new_user.save()

        authors = load_from_json('authors')
        Author.objects.all().delete()
        for author in authors:
            instance = User.objects.filter(pk=author['username'])[0]
            new_author = Author(uid=author['pk'], username=instance)
            new_author.save()

        books = load_from_json('books')
        Book.objects.all().delete()
        for book in books:
            instance = Author.objects.filter(pk=book['authors'])[0]
            uuid_item = uuid.UUID(book['pk'])
            new_book = Book(uid=uuid_item, name=book['name'])
            new_book.save()
            new_book.authors.add(instance)

        projects = load_from_json('projects')
        Project.objects.all().delete()
        for project in projects:
            # for number in enumerate(len(project['authors'])):
            print(len(project['authors']))
            instance = Author.objects.filter(pk=project['authors'])[0]
            print(instance)
            uuid_item = uuid.UUID(project['pk'])
            print(uuid_item)
            new_project = Project(uid=uuid_item,
                                  name=project['name'],
                                  link=project['link'])
            new_project.save()
            # new_project.authors.add(instance)
