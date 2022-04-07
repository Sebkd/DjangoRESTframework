from django.test import TestCase
import json
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate
from django.contrib.auth.models import User

from todoapp.views import ToDoCustomMixinViewSet


class TestToDoCustomMixinViewSet(TestCase):
    def test_get_list_with_auth(self):
        factory = APIRequestFactory() #rhfqyt htlrj bcgjkmpetncz
        request = factory.get('/api/todo/')
        admin = User.objects.create_superuser('admin', 'admin@admin.com', '123')
        force_authenticate(request, admin)
        view = ToDoCustomMixinViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

# Create your tests here.
from django.test import TestCase

# Create your tests here.
