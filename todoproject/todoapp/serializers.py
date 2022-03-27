from rest_framework.relations import SlugRelatedField, StringRelatedField
from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer

from authors.models import Author
from authors.serializers import SimpleAuthorModelSerializer, AuthorModelSerializer, AuthorStringRelatedField
from todoapp.models import Project, ToDo


class SimpleProjectModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ['name',]


class ProjectModelSerializer(HyperlinkedModelSerializer):
    # authors = SimpleAuthorModelSerializer(many=True)
    authors = SlugRelatedField(many=True, slug_field='username', queryset=Author.objects.all())

    class Meta:
        model = Project
        fields = '__all__'


class ProjectStringRelatedField(StringRelatedField):
    class Meta:
        model = Project


class ToDoModelSerializer(HyperlinkedModelSerializer):
    author = AuthorStringRelatedField()
    project = ProjectStringRelatedField()

    class Meta:
        model = ToDo
        fields = '__all__'
