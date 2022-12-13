from django.test import SimpleTestCase
from django.urls import reverse, resolve
from core.views import home,usrreg,pfle
from django.contrib.auth import views as v

class TestUrls(SimpleTestCase):
    def test_home_url_is_resolved(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, home)

    def test_register_url_is_resolved(self):
        url=reverse('register')
        self.assertEquals(resolve(url).func, usrreg)

    def test_login_url_is_resolved(self):
        url=reverse('login')
        self.assertEquals(resolve(url).func.view_class, v.LoginView)

    def test_logout_url_is_resolved(self):
        url=reverse('logout')
        self.assertEquals(resolve(url).func.view_class, v.LogoutView)
        
    def test_profile_url_is_resolved(self):
        url=reverse('profile')
        self.assertEquals(resolve(url).func, pfle)
