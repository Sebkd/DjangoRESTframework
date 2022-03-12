from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.generics import CreateAPIView, ListAPIView

from rest_framework import mixins
from .filters import AuthorFilter

from .models import Author, Book, Biography, Article
from .serializers import AuthorModelSerializer, BookModelSerializer, BiographyModelSerializer, ArticleModelSerializer, \
    SmallAuthorModelSerializer

from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer, StaticHTMLRenderer
from rest_framework.parsers import JSONParser


#
# class AuthorApimixin(mixins.CreateModelMixin,
#                      mixins.RetrieveModelMixin,
#                      mixins.UpdateModelMixin,
#                      mixins.DestroyModelMixin,
#                      mixins.ListModelMixin,
#                      GenericViewSet):  # просто посмотреть mixin
#     queryset = Author.objects.all()
#     serializer_class = AuthorModelSerializer
#
#
# class AuthorApiModelViewSet(ModelViewSet):  # просто посмотреть ModelViewSet
#     queryset = Author.objects.all()
#     serializer_class = AuthorModelSerializer
#
#     def list(self, request, *args, **kwargs):
#         print('тест изменненого list')
#         return super().list(request, *args, **kwargs)
#
#
# class AuthorApiViewSet(viewsets.ViewSet):  # здесь уже есть методы get put delete
#
#     @action(detail=False, methods=['get'])  # на метод get будет вызван метод change_password
#     def change_password(self, request):  # detail показывает работаем мы со всей выборкой. Если нужен один то нужно
#         # использовать pk:
#         # @action(detail=True, methods=['get'])
#         # def change_password(self, request, pk):
#         return Response('Test methods')
#
#     def list(self, request):
#         authors = Author.objects.all()
#         serializer = SmallAuthorModelSerializer(authors, many=True)
#         return Response(serializer.data)
#
#
# class AuthorCreateApiView(CreateAPIView):  # возвращает создание через post + можно добавить и сразу ListAPIView
#     renderer_classes = [JSONRenderer]  # просто добавляют обработчики
#     queryset = Author.objects.all()
#     serializer_class = AuthorModelSerializer
#
#
# class AuthorListApiView(ListAPIView):  # возвращает обзор через get
#     renderer_classes = [JSONRenderer]  # если нужно для одного контроллера
#     queryset = Author.objects.all()
#     serializer_class = AuthorModelSerializer
#
#
# class AuthorApiView(APIView):  # просто посмотреть APIView
#
#     def get(self, request):
#         authors = Author.objects.all()
#         serializer = SmallAuthorModelSerializer(authors, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         return Response('POST ответ на него')
#

# @api_view(['GET'])
# @renderer_classes([JSONRenderer])
# def article_view(request):
#     articles = Article.objects.all()
#     serializer = ArticleSerializer(articles, many=True)
#     return Response(serializer.data)

class AuthorCustomMixinViewSet(
    # mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    # mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    GenericViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer  # с помощью какого сериализатора необходимо преобразовать в JSON
    filterset_class = AuthorFilter


class AuthorModelViewSet(ModelViewSet):  # ModelViewSet реализует CRUD
    # username = filters.CharFilter(lookup_expr='contains')
    # renderer_classes = [JSONRenderer, BrowsableAPIRenderer] # если нужно для одного контроллера
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer  # с помощью какого сериализатора необходимо преобразовать в JSON
    filterset_class = AuthorFilter

    # serializer_class = SmallAuthorModelSerializer # для поиска через url (kwarg)
    # filterset_fields = ['username']

    # def get_queryset(self):# переопределение метода
    #     param = self.request.headers.get('param') # для поиска через ?param
    #     newparam = self.kwargs['newparam'] # для поиска через url (kwarg)
    #     # return Author.objects.filter(first_name__contains=param)
    #     return Author.objects.filter(first_name__contains=newparam) # для поиска через url (kwarg)

    def destroy(self, request, *args, **kwargs):  # переопределения метода удаления
        return Response({'forbidden': 'Запрещено удалять'}, status=status.HTTP_403_FORBIDDEN)

    def create(self, request, *args, **kwargs):  # переопределения метода удаления
        return Response({'forbidden': 'Запрещено добавлять'}, status=status.HTTP_403_FORBIDDEN)


class BookModelViewSet(ModelViewSet):  # ModelViewSet реализует CRUD
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer  # с помощью какого сериализатора необходимо преобразовать в JSON


class ArticleModelViewSet(ModelViewSet):  # ModelViewSet реализует CRUD
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer  # с помощью какого сериализатора необходимо преобразовать в JSON


class BiographyModelViewSet(ModelViewSet):  # ModelViewSet реализует CRUD
    queryset = Biography.objects.all()
    serializer_class = BiographyModelSerializer  # с помощью какого сериализатора необходимо преобразовать в JSON
