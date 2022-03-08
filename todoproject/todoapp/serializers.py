from rest_framework.serializers import HyperlinkedModelSerializer

from authors.serializers import SimpleAuthorModelSerializer
from todoapp.models import Project, ToDo


class ProjectModelSerializer(HyperlinkedModelSerializer):
    authors = SimpleAuthorModelSerializer(many=True)

    class Meta:
        model = Project
        fields = '__all__'


class ToDoModelSerializer(HyperlinkedModelSerializer):
    author = SimpleAuthorModelSerializer()

    class Meta:
        model = ToDo
        fields = '__all__'
