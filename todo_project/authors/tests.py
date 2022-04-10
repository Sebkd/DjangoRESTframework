from django.test import TestCase
import json
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient
from django.contrib.auth.models import User

from authors.models import Author
from authors.views import AuthorCustomMixinViewSet


class TestAuthorMixinViewSet(TestCase):
    def test_get_list_with_auth(self):
        factory = APIRequestFactory()
        request = factory.get('/api/authors/')
        admin = User.objects.create_superuser('admin', 'admin@admin.com', '123')
        force_authenticate(request, admin)
        view = AuthorCustomMixinViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_detail_wo_auth(self):
        admin = User.objects.create_superuser('admin', 'admin@admin.com', '123')
        author = Author.objects.create(username=admin)
        client = APIClient()
        response = client.get(f'/api/authors/{author.uid}/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_detail_with_auth(self):
        admin = User.objects.create_superuser('admin', 'admin@admin.com', '123')
        author = Author.objects.create(username=admin)
        client = APIClient()
        client.login(username='admin', password='123')
        response = client.get(f'/api/authors/{author.uid}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        client.logout()

# Create your tests here.
