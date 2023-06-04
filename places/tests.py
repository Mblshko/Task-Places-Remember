from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Places


class PlacesTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='test_password')
        self.client.force_login(self.user)
        self.place = Places.objects.create(title='Test title',  description='Content test', author=self.user)
        self.place_data = {'title': 'Test title 2', 'description': 'Content test 2', 'author': self.user}

    def test_index_no_authenticated(self):
        '''Тест главной страницы без авторизации'''
        self.client.logout()
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'places/index.html')

    def test_index_authenticated(self):
        '''Тест главной страницы с авторизацией'''
        response = self.client.get(reverse('index'))
        self.assertRedirects(response, reverse('list_places'))

    def test_list_places_authenticated(self):
        '''Тест PlacesView c авторизацией'''
        response = self.client.get(reverse('list_places'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['places']), 1)
        self.assertTemplateUsed(response, 'places/list.html')

    def test_list_places_no_authenticated(self):
        '''Тест PlacesView без авторизации'''
        self.client.logout()
        response = self.client.get(reverse('list_places'))
        self.assertRedirects(response, reverse('index'))

    def test_add_place_authenticated(self):
        '''Тест AddPlace c авторизацией'''
        response = self.client.post(reverse('add_place'), data=self.place_data)
        self.assertRedirects(response, reverse('list_places'))
        self.assertTrue(Places.objects.filter(title=self.place_data['title']).exists())

    def test_add_place_no_authenticated(self):
        '''Тест AddPlace без авторизации'''
        self.client.logout()
        response = self.client.get(reverse('add_place'))
        self.assertRedirects(response, reverse('index'))
