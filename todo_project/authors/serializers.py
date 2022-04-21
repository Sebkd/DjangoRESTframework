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

class UserSerializers(ModelSerializer):  # work model
    class Meta:
        model = User
        fields = ['username', 'is_superuser', 'is_staff', ]


class UserSimpleSerializers(ModelSerializer):  # work model
    class Meta:
        model = User
        fields = ['username', ]


class AuthorUserModelSerializer(ModelSerializer):  # work model for Author ModelSerializer
    # username = UserSerializers()
    # username = User.objects.all()
    username = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')

    class Meta:
        model = Author
        fields = '__all__'

    def create(self, validated_data):
        return Author.objects.create(**validated_data)


class AuthorUserSimpleModelSerializer(ModelSerializer):  # work model for Author
    username = UserSimpleSerializers()

    class Meta:
        model = Author
        fields = '__all__'

    def create(self, validated_data):
        return Author.objects.create(**validated_data)


class AuthorModelSerializer(ModelSerializer):
    username = serializers.SlugRelatedField(queryset=get_user_model().objects.all(), slug_field='username')

    class Meta:
        model = Author
        # fields = '__all__'
        fields = ['username', ]

    def create(self, validated_data):
        return Author.objects.create(**validated_data)


class AuthorStringRelatedField(StringRelatedField, ABC):
    class Meta:
        model = Author
        fields = '__all__'


class BiographyModelSerializer(HyperlinkedModelSerializer):
    author = SimpleAuthorModelSerializer()

    class Meta:
        model = Biography
        fields = '__all__'


# class BookModelSerializer(ModelSerializer):
class BookModelSerializer(HyperlinkedModelSerializer): #work model
    # authors = SimpleAuthorModelSerializer(many=True)
    # authors = StringRelatedField(many=True, queryset=Author.objects.all())
    authors = SlugRelatedField(many=True, slug_field='uid', queryset=Author.objects.all())

    # authors = RelatedField(many=True, queryset=Author.objects.all())

    class Meta:
        model = Book
        fields = '__all__'


class ArticleModelSerializer(HyperlinkedModelSerializer):
    author = SimpleAuthorModelSerializer()

    class Meta:
        model = Article
        fields = '__all__'
