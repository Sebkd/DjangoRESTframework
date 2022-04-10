from pprint import pprint

from django.test import TestCase
import json
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate
from django.contrib.auth.models import User

from authors.models import Author
from todoapp.models import Project, ToDo
from todoapp.views import ToDoCustomMixinViewSet

from mixer.backend.django import mixer


class TestToDoCustomMixinViewSet(TestCase):
    def test_get_list_with_auth(self):
        factory = APIRequestFactory() #rhfqyt htlrj bcgjkmpetncz
        request = factory.get('/api/todo/')
        admin = User.objects.create_superuser('admin', 'admin@admin.com', '123')
        force_authenticate(request, admin)
        view = ToDoCustomMixinViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_detail_with_auth_on(self):
        admin = User.objects.create_superuser('admin', 'admin@admin.com', '123')
        self.client.login(username='admin', password='123')
        author = Author.objects.create(username=admin)
        project = Project.objects.create(name='Luna transporter', authors=author)
        todo = ToDo.objects.create(project=project, content='Fanny', author=author)
        self.client.login(username='admin', password='123')
        response = self.client.put(f'/api/todo/{todo.uid}/', {
            'content' : 'noFunny',
            'author' : todo.author.uid,
            'project' : todo.project.uid
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK) #AssertionError: 415 != 200

        todo = ToDo.objects.get(uid=todo.uid)
        self.assertEqual(todo.content, 'noFunny')

    def test_get_detail_with_auth_on_mixer(self):
        admin = User.objects.create_superuser('admin', 'admin@admin.com', '123')
        todo = mixer.blend(ToDo, content='Funny')
        print(todo.uid, '::' ,todo.project, '::' ,todo.author, '::' ,todo.content)
        self.client.login(username='admin', password='123')
        response = self.client.get(f'/api/todo/{todo.uid}')
        self.assertEqual(response.status_code, status.HTTP_200_OK) #AssertionError: 415 != 200
        response_todo = json.loads(response.content)
        self.assertEqual(response_todo['content'], 'Funny')

# Create your tests here.
from django.test import TestCase

# Create your tests here.
