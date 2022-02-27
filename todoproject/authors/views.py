from rest_framework.viewsets import ModelViewSet
from .models import Author
from .serializers import AuthorModelSerializer

class AuthorModelViewSet(ModelViewSet): # ModelViewSet реализует CRUD
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer # с помощью какого сериализатора необходимо преобразовать в JSON

# Create your views here.
