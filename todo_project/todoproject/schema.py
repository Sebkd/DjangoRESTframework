import graphene
from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType

from authors.models import Book, Author
from todoapp.models import Project, ToDo


class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = '__all__'


class ToDoType(DjangoObjectType):
    class Meta:
        model = ToDo
        fields = '__all__'


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        fields = '__all__'


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()
        fields = '__all__'


class Query(graphene.ObjectType):
    # all_books = graphene.List(BookType)
    all_todos = graphene.List(ToDoType)
    all_projects = graphene.List(ProjectType)
    all_authors = graphene.List(AuthorType)
    all_users = graphene.List(UserType)


    def resolve_all_projects(self, info):  # graphene ищет resolve_
        return Project.objects.all()

    def resolve_all_todos(self, info):  # graphene ищет resolve_
        return ToDo.objects.all()

    def resolve_all_authors(self, info):  # graphene ищет resolve_
        return Author.objects.all()

    def resolve_all_users(self, info):  # graphene ищет resolve_
        return get_user_model().objects.all()

    # hello = graphene.String(default_value='Hi')


schema = graphene.Schema(query=Query)
