from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Author, Article, Biography, Book


class AuthorModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = (
            'username',
            'first_name',
            'last_name',
            'birthday_year',
            'email',
        )


class BiographyModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Biography
        fields = (
            'text',
            'author',
        )



class BookModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = (
            'name',
            'author',
        )



class ArticleModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = (
            'name',
            'author',
        )
