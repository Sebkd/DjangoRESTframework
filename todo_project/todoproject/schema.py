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
    author_by_id = graphene.Field(AuthorType, uuid=graphene.UUID(required=True))
    books_by_author_name = graphene.List(BookType, name=graphene.String(required=True))
    projects_by_author_name = graphene.List(ProjectType, authors=graphene.String(required=True))
    authors_by_project_name = graphene.List(AuthorType, project=graphene.String(required=True))

    def resolve_authors_by_project_name(self, info, project=None):
        projects = Project.objects.filter(name__icontains=project).values('authors')
        # authors = Author.objects.filter()
        # return authors

    def resolve_projects_by_author_name(self, info, authors=None):
        projects = Project.objects.all()
        if authors:
            projects = projects.filter(authors__username__username=authors)
        return projects

    def resolve_all_projects(self, info):  # graphene ищет resolve_
        return Project.objects.all()

    def resolve_all_todos(self, info):  # graphene ищет resolve_
        return ToDo.objects.all()

    def resolve_all_authors(self, info):  # graphene ищет resolve_
        return Author.objects.all()

    def resolve_all_users(self, info):  # graphene ищет resolve_
        return get_user_model().objects.all()

    def resolve_author_by_id(self, info, uuid):
        try:
            return Author.objects.get(uid=uuid)
        except Author.DoesNotExist:
            return None

    def resolve_books_by_author_name(self, info, name=None):
        books = Book.objects.all()
        if name:
            books = books.filter(author__name=name)
        return books

    # hello = graphene.String(default_value='Hi')

# class AuthorMutation(graphene.Mutation):
#     class Arguments:
#        birthday_year = graphene.Int(required=True)
#        id = graphene.ID()
#
#     author =  graphene.Field(AuthorType)
#
#     @classmethod
#     def mutate(cls, root, info, birthday_year, id):
#         author = Author.objects.get(pk=id)
#         author.birthday_year = birthday_year
#         author.save()
#         return AuthorMutation(author=author)
#
# class Mutation(graphene.ObjectType):
#     update_author = AuthorMutation.Field()

# schema = graphene.Schema(query=Query, mutation=Mutation)
schema = graphene.Schema(query=Query)
