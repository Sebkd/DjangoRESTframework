from rest_framework.serializers import StringRelatedField, PrimaryKeyRelatedField
from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from .models import Author, Article, Biography, Book




# HyperlinkedModelSerializer

class SimpleAuthorModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', ]


class AuthorModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Author
        # exclude = ['url']
        fields = '__all__'


class BiographyModelSerializer(HyperlinkedModelSerializer):
    author = SimpleAuthorModelSerializer()

    class Meta:
        model = Biography
        fields = '__all__'


class BookModelSerializer(ModelSerializer):
    # authors = SimpleAuthorModelSerializer(many=True)
    authors = StringRelatedField(many=True)
    # authors = AuthorModelSerializer(many=True)

    class Meta:
        model = Book
        fields = '__all__'


class ArticleModelSerializer(HyperlinkedModelSerializer):
    author = SimpleAuthorModelSerializer()

    class Meta:
        model = Article
        fields = '__all__'
