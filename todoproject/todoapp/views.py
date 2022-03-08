from rest_framework.viewsets import ModelViewSet

from todoapp.models import Project, ToDo
from todoapp.serializers import ProjectModelSerializer, ToDoModelSerializer


class ProjectModelViewSet(ModelViewSet):  # ModelViewSet реализует CRUD
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer  # с помощью какого сериализатора необходимо преобразовать в JSON


class ToDoModelViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer