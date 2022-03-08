from rest_framework.viewsets import ModelViewSet
from .models import Author, Book, Biography, Article
from .serializers import AuthorModelSerializer, BookModelSerializer, BiographyModelSerializer, ArticleModelSerializer


class AuthorModelViewSet(ModelViewSet): # ModelViewSet реализует CRUD
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer # с помощью какого сериализатора необходимо преобразовать в JSON


class BookModelViewSet(ModelViewSet): # ModelViewSet реализует CRUD
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer # с помощью какого сериализатора необходимо преобразовать в JSON


class ArticleModelViewSet(ModelViewSet): # ModelViewSet реализует CRUD
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer # с помощью какого сериализатора необходимо преобразовать в JSON


class BiographyModelViewSet(ModelViewSet): # ModelViewSet реализует CRUD
    queryset = Biography.objects.all()
    serializer_class = BiographyModelSerializer # с помощью какого сериализатора необходимо преобразовать в JSON
