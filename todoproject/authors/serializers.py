from abc import ABC

from django.contrib.auth import get_user_model
from rest_framework import serializers

from rest_framework.relations import HyperlinkedRelatedField, SlugRelatedField, RelatedField
from rest_framework.serializers import StringRelatedField, PrimaryKeyRelatedField
from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from .models import Author, Article, Biography, Book

from django.contrib.auth.models import User, AbstractUser


# HyperlinkedModelSerializer
class SmallAuthorModelSerializer(ModelSerializer):  # для APIView
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', ]


class SimpleAuthorModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', ]



# class SimpleUserModelSerializer(ModelSerializer):
#     class Meta:
#         model = User
#         fields = 'username'

class AuthorModelSerializer(ModelSerializer):#work model
    # username = serializers.CharField(source='username.username', read_only=False)
    # username = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all(), source='username.username', )
    username = serializers.SlugRelatedField(queryset = get_user_model().objects.all(),slug_field = 'username')
    class Meta:
        model = Author
        # fields = ['username',]
        fields = '__all__'

    def create(self, validated_data):
        return Author.objects.create(**validated_data)


class AuthorStringRelatedField(StringRelatedField, ABC):#work in todo
    class Meta:
        model = Author
        fields = '__all__'



class BiographyModelSerializer(HyperlinkedModelSerializer):
    author = SimpleAuthorModelSerializer()

    class Meta:
        model = Biography
        fields = '__all__'


# class BookModelSerializer(ModelSerializer):
class BookModelSerializer(HyperlinkedModelSerializer):
    # authors = SimpleAuthorModelSerializer(many=True)
    # authors = StringRelatedField(many=True, queryset=Author.objects.all())
    authors = SlugRelatedField(many=True, slug_field='username', queryset=Author.objects.all())

    # authors = RelatedField(many=True, queryset=Author.objects.all())

    class Meta:
        model = Book
        fields = '__all__'


class ArticleModelSerializer(HyperlinkedModelSerializer):
    author = SimpleAuthorModelSerializer()

    class Meta:
        model = Article
        fields = '__all__'
