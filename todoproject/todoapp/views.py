from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination

from .filters import ProjectFilter, ToDoFilter

from todoapp.models import Project, ToDo
from todoapp.serializers import ProjectModelSerializer, ToDoModelSerializer


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class ToDoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class ProjectModelViewSet(ModelViewSet):  # ModelViewSet реализует CRUD Work model
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer  # с помощью какого сериализатора необходимо преобразовать в JSON
    pagination_class = ProjectLimitOffsetPagination
    filterset_class = ProjectFilter


# class ProjectCustomFilterModelViewSet(ModelViewSet):  # используем filters
#     queryset = Project.objects.all()
#     serializer_class = ProjectModelSerializer
#     filterset_class = ProjectFilter


class ToDoModelViewSet(ModelViewSet):#work model
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer
    pagination_class = ToDoLimitOffsetPagination
    filterset_class = ToDoFilter

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()



class ToDoCustomFilterModelViewSet(ModelViewSet):  # используем filters
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer
    filterset_class = ToDoFilter
    pagination_class = ToDoLimitOffsetPagination
