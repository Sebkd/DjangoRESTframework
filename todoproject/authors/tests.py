from django.test import TestCase
import json
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate
from django.contrib.auth.models import User

from authors.views import AuthorCustomMixinViewSet

class TestAuthorMixinViewSet(TestCase):
    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/authors/')
        admin = User.objects.create_superuser('admin', 'admin@admin.com', '123')
        force_authenticate(request, admin)
        view = AuthorCustomMixinViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

# Create your tests here.
