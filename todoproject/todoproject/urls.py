"""todoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from authors.views import AuthorModelViewSet, ArticleModelViewSet, BookModelViewSet, BiographyModelViewSet, \
    AuthorCustomMixinViewSet
# from authors.views import AuthorApiView, AuthorListApiView, AuthorApiViewSet, AuthorApiModelViewSet
from todoapp.views import ProjectModelViewSet, ToDoModelViewSet, \
    ToDoCustomFilterModelViewSet

router = DefaultRouter()  # определяем роутер
router.register('authors',
                AuthorCustomMixinViewSet)  # регистрируем роутер за authors и определяем что он сам сделаем все пути
# router.register('biography',
#                 BiographyModelViewSet)  # регистрируем роутер за biography и определяем что он сам сделаем все пути
router.register('book', BookModelViewSet)  # регистрируем роутер за book и определяем что он сам сделаем все пути
# router.register('article',
#                 ArticleModelViewSet)  # регистрируем роутер за article и определяем что он сам сделаем все пути

router.register('project',
                ProjectModelViewSet)
router.register('todo',
                ToDoModelViewSet)

# router.register('testviewset', # просто посмотреть AuthorApiViewSet
#                 AuthorApiViewSet, basename='api') # viewset не может генерировать basename поэтому его нужно вручную
#
# router.register('testmodelviewset',
#                 AuthorApiModelViewSet)  # просто посмотреть AuthorApiModelViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),  # собственно он сам далее после api/ пропишет все пути по CRUD
    # path('apiview/', AuthorApiView.as_view()), # просто посмотреть APIView
    # path('apilistview/', AuthorListApiView.as_view()), # просто посмотреть AuthorListApiView
    # path('author/<str:newparam>/', AuthorModelViewSet.as_view({'get': 'list'})), # просто посмотреть get_queryset с kwarg
]
