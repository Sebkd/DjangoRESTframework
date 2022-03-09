from rest_framework.viewsets import ModelViewSet
from .models import Author, Book, Biography, Article
from .serializers import AuthorModelSerializer, BookModelSerializer, BiographyModelSerializer, ArticleModelSerializer

from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer, StaticHTMLRenderer
from rest_framework.parsers import JSONParser


class AuthorModelViewSet(ModelViewSet):  # ModelViewSet реализует CRUD
    # renderer_classes = [JSONRenderer, BrowsableAPIRenderer] # если нужно для одного контроллера
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer  # с помощью какого сериализатора необходимо преобразовать в JSON


class BookModelViewSet(ModelViewSet):  # ModelViewSet реализует CRUD
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer  # с помощью какого сериализатора необходимо преобразовать в JSON


class ArticleModelViewSet(ModelViewSet):  # ModelViewSet реализует CRUD
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer  # с помощью какого сериализатора необходимо преобразовать в JSON


class BiographyModelViewSet(ModelViewSet):  # ModelViewSet реализует CRUD
    queryset = Biography.objects.all()
    serializer_class = BiographyModelSerializer  # с помощью какого сериализатора необходимо преобразовать в JSON
