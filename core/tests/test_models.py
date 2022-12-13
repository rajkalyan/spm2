from django.test import TestCase
from core.models import User

class TestModels(TestCase):
    def setUp(self) -> None:
        self.user1=User.objects.create(first_name="Manish",
        last_name="Valeti",email="manishvaleti@gmail.com",username="manish",mobilenumber="9121847678",address="miyapur")

    def test_user_on_creation(self):
        self.assertEquals(self.user1,'manish')
