from django.test import TestCase
from .models import HubDoggyModel


class TestHub(TestCase):

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_donepage(self):
        response = self.client.get('/done')
        self.assertEqual(response.status_code, 200)

    def test_doggypage(self):
        HubDoggyModel.objects.create(id=1, name='Big Mike', age_old=2, months_old=3, gender='Boy', slug='big-mike')
        dog = HubDoggyModel.objects.get(id=1)
        response = self.client.get(f'/hub/{dog.slug}{dog.id}')
        self.assertEqual(response.status_code, 200)

    def test_hubpage(self):
        response = self.client.get('/hub')
        self.assertEqual(response.status_code, 200)

