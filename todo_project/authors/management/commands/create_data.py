import os
import uuid
from pathlib import Path

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group, Permission
from django.db.models import Q
from rest_framework.utils import json

from authors.models import Author, Book
from todoapp.models import Project, ToDo

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = Path(CURRENT_DIR).parent.parent
JSON_PATH = os.path.dirname(os.path.abspath(PARENT_DIR)) + '/jsons'
# JSON_PATH = "2_step_2_for_test_django_and_migrations/DjangoRESTframework/todo_project/jsons"


def load_from_json(file_nm):
    """
    """
    with open(os.path.join(JSON_PATH, file_nm + '.json'), 'r', encoding='utf-8') as ld_file:
        return json.load(ld_file)


class Command(BaseCommand):

    def handle(self, *args, **options):

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
            new_book = Book(uid=uuid_item, name=book['name'],)
            new_book.save()
            new_book.authors.add(instance)

        projects = load_from_json('projects')
        Project.objects.all().delete()
        for project in projects:
            instance = [pk for pk in Author.objects.filter(pk__in=project['authors'])]
            uuid_item = uuid.UUID(project['pk'])
            new_project = Project(uid=uuid_item,
                                  name=project['name'],
                                  link=project['link'])
            new_project.save()
            new_project.authors.set(instance)

        todos = load_from_json('todos')
        ToDo.objects.all().delete()
        for todo in todos:
            author = Author.objects.filter(pk=todo['author'])[0]
            project = Project.objects.filter(pk=todo['project'])[0]
            uuid_item = uuid.UUID(todo['pk'])
            new_todo = ToDo(uid=uuid_item,
                            content=todo['content'],
                            project_id=project.uid,
                            author_id=author.uid,)
            new_todo.save()
        #права

        #книги
        add_book = Permission.objects.get(codename='add_book')
        change_book = Permission.objects.get(codename='change_book')
        delete_book = Permission.objects.get(codename='delete_book')

        #авторы
        add_author = Permission.objects.get(codename='add_author')
        change_author = Permission.objects.get(codename='change_author')
        delete_author = Permission.objects.get(codename='delete_author')

        #проекты
        add_project = Permission.objects.get(codename='add_project')
        change_project = Permission.objects.get(codename='change_project')
        delete_project = Permission.objects.get(codename='delete_project')

        #заметки
        add_todo = Permission.objects.get(codename='add_todo')
        change_todo = Permission.objects.get(codename='change_todo')
        delete_todo = Permission.objects.get(codename='delete_todo')

        Group.objects.all().delete()
        #Группы
        #Devops
        devops_staff = Group.objects.create(name='Разработчики')

        #права devops: разработчики имеют все права на модель ToDo,
        # могут просматривать модели Project и Author;
        devops_staff.permissions.add(add_todo)
        devops_staff.permissions.add(change_todo)
        devops_staff.permissions.add(delete_todo)

        #Projectowners
        project_owners_staff = Group.objects.create(name='Владельцы проектов')

        #права Projectowners: владельцы проектов имеют права на просмотр модели
        # Author и все права на модель Project и ToDo
        project_owners_staff.permissions.add(add_todo)
        project_owners_staff.permissions.add(change_todo)
        project_owners_staff.permissions.add(delete_todo)

        project_owners_staff.permissions.add(add_project)
        project_owners_staff.permissions.add(change_project)
        project_owners_staff.permissions.add(delete_project)

        owners = User.objects.filter(Q(username__contains ='Nastya_user') |
                                     Q(username__contains ='Dmitry_user') |
                                     Q(username__contains ='Andrey_user'))
        for owner in owners:
            owner.groups.add(project_owners_staff)
            owner.save()

        devops = User.objects.filter(username__contains='bot')
        for devop in devops:
            devop.groups.add(devops_staff)
            devop.save()

