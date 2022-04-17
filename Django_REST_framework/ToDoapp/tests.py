import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, \
    APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
from django.contrib.auth.models import User

from ToDoapp.models import Project
from users.views import UserModelViewSet
from users.models import User


class TestUserViewSet(TestCase):

    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/users/')
        view = UserModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_guest(self):
        factory = APIRequestFactory()
        request = factory.post('/api/users', {'first_name': 'Александр',
                                              'last_name': 'Сергеевич',
                                              'username': 'pushkin',
                                              'email': 'mail@mail.test'},
                               format='json')
        view = UserModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_admin(self):
        factory = APIRequestFactory()
        request = factory.post('/api/users', {'first_name': 'Александр',
                                              'last_name': 'Сергеевич',
                                              'username': 'pushkin',
                                              'email': 'mail@mail.test'},
                               format='json')
        admin = User.objects.create_superuser('admin', 'admin@mail.test',
                                              'admin123456')
        force_authenticate(request, admin)
        view = UserModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_detail(self):
        user = User.objects.create(first_name='Александр',
                                   last_name='Сергеевич',
                                   username='pushkin',
                                   email='mail@mail.test')
        client = APIClient()
        response = client.get(f'/api/users/{user.uid}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_guest(self):
        user = User.objects.create(first_name='Александр',
                                   last_name='Сергеевич',
                                   username='pushkin',
                                   email='mail@mail.test')
        client = APIClient()
        response = client.put(f'/api/users/{user.uid}/',
                              {'first_name': 'Алеша',
                               'last_name': 'Попович',
                               'username': 'pop',
                               'email': 'pop@mail.test'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_edit_admin(self):
        user = User.objects.create(first_name='Александр',
                                   last_name='Сергеевич',
                                   username='pushkin',
                                   email='mail@mail.test')
        client = APIClient()
        admin = User.objects.create_superuser('admin', 'admin@mail.test',
                                              'admin123456')
        client.login(username='admin', password='admin123456')
        response = client.put(f'/api/users/{user.uid}/',
                              {'first_name': 'Алеша',
                               'last_name': 'Попович',
                               'username': 'pop',
                               'email': 'pop@mail.test'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        user = User.objects.get(uid=user.uid)
        self.assertEqual(user.first_name, 'Алеша')
        self.assertEqual(user.last_name, 'Попович')
        self.assertEqual(user.username, 'pop')
        self.assertEqual(user.email, 'pop@mail.test')
        client.logout()


class TestProjectViewSet(APITestCase):

    def test_get_list(self):
        response = self.client.get('/api/projects/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_admin(self):
        # user = User.objects.create(first_name='Александр',
        #                            last_name='Сергеевич',
        #                            username='pushkin',
        #                            email='mail@mail.test')
        # project = Project.objects.create(name='TestPrName',
        #                                  link='https://todo.sep.bm/')
        # project.worker.add(user)
        project = mixer.blend(Project, name='Тест',
                              link='https://todo.sep.bm/')
        # print(project.name, project.link)
        admin = User.objects.create_superuser('admin', 'admin@mail.test',
                                              'admin123456')
        self.client.login(username='admin', password='admin123456')
        response = self.client.put(f'/api/projects/{project.uid}/',
                                   {
                                       'name': 'изменен',
                                       'link': "https://todo.updating.tel/"
                                   })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        project = Project.objects.get(uid=project.uid)
        self.assertEqual(project.name, 'изменен')
        self.assertEqual(project.link, 'https://todo.updating.tel/')
