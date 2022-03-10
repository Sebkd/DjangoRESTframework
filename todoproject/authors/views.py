from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView, ListAPIView

from .models import Author, Book, Biography, Article
from .serializers import AuthorModelSerializer, BookModelSerializer, BiographyModelSerializer, ArticleModelSerializer, \
    SmallAuthorModelSerializer

from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer, StaticHTMLRenderer
from rest_framework.parsers import JSONParser

class AuthorCreateApiView(CreateAPIView): # возвращает создание через post + можно добавить и сразу ListAPIView
    renderer_classes = [JSONRenderer] # просто добавляют обработчики
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer

class AuthorListApiView(ListAPIView): # возвращает обзор через get
    renderer_classes = [JSONRenderer] # если нужно для одного контроллера
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer



class AuthorApiView(APIView):  # просто посмотреть APIView

    def get(self, request):
        authors = Author.objects.all()
        serializer = SmallAuthorModelSerializer(authors, many=True)
        return Response(serializer.data)

    def post(self, request):
        return Response('POST ответ на него')


# @api_view(['GET'])
# @renderer_classes([JSONRenderer])
# def article_view(request):
#     articles = Article.objects.all()
#     serializer = ArticleSerializer(articles, many=True)
#     return Response(serializer.data)


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
