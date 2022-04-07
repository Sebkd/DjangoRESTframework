from abc import ABC
from rest_framework import serializers

from rest_framework.relations import SlugRelatedField, StringRelatedField
from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer

from authors.models import Author
from authors.serializers import SimpleAuthorModelSerializer, AuthorModelSerializer, AuthorStringRelatedField
from todoapp.models import Project, ToDo


class SimpleProjectModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ['name',]


class ProjectModelSerializer(HyperlinkedModelSerializer): #work model
    # authors = SimpleAuthorModelSerializer(many=True)
    # authors = SlugRelatedField(many=True, slug_field='username', queryset=Author.objects.all())
    authors = serializers.SlugRelatedField(queryset=Author.objects.all(), slug_field='uid') # выборка один из многого

    class Meta:
        model = Project
        fields = '__all__'

    def create(self, validated_data):
        return Project.objects.create(**validated_data)


class ProjectStringRelatedField(StringRelatedField, ABC):
    class Meta:
        model = Project


class ToDoModelSerializer(HyperlinkedModelSerializer):
    author = AuthorStringRelatedField()
    project = ProjectStringRelatedField()

    class Meta:
        model = ToDo
        fields = '__all__'

class ToDoHyperModelSerializer(HyperlinkedModelSerializer):# work model HyperlinkedModelSerializer
    author = serializers.SlugRelatedField(queryset=Author.objects.all(), slug_field='uid') # выборка один из многого
    project = serializers.SlugRelatedField(queryset=Project.objects.all(), slug_field='name') # выборка один из многого
    # author = AuthorStringRelatedField()
    # project = ProjectStringRelatedField()

    class Meta:
        model = ToDo
        fields = '__all__'

        # fields = ['project', 'author', 'content', ]
