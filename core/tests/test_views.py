from urllib import response
from django.test import TestCase, Client
from django.urls import reverse
from core.models import User
import json

class TestViews(TestCase):
    def setUp(self) -> None:
        self.client=Client()
        self.home_url=reverse('index')
        self.register_url=reverse('register')
        self.login_url=reverse('login')
        self.logout_url=reverse('logout')

    def test_home_GET(self):
        response=self.client.get(self.home_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'html/index.html')
    
    def test_register_GET(self):
        response=self.client.get(self.register_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'html/register.html')
    
    def test_login_GET(self):
        response=self.client.get(self.login_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'html/login.html')

    def test_logout_GET(self):
        response=self.client.get(self.logout_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'html/logout.html')
    
