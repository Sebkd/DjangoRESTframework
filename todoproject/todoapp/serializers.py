from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import HyperlinkedModelSerializer

from authors.models import Author
from authors.serializers import SimpleAuthorModelSerializer
from todoapp.models import Project, ToDo


class SimpleProjectModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = 'name'


class ProjectModelSerializer(HyperlinkedModelSerializer):
    # authors = SimpleAuthorModelSerializer(many=True)
    authors = SlugRelatedField(many=True, slug_field='username', queryset=Author.objects.all())

    class Meta:
        model = Project
        fields = '__all__'


class ToDoModelSerializer(HyperlinkedModelSerializer):
    # author = SimpleAuthorModelSerializer()
    # project = SimpleProjectModelSerializer()

    class Meta:
        model = ToDo
        fields = '__all__'
