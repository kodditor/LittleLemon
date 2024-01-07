from django.test import TestCase
from Restaurant.models import menu

class MenuTest(TestCase):
    def test_menu(self):
        self.item = menu.objects.create(id=99, title="IceCream", price=80, inventory=100)
        self.assertEqual(self.item.__str__(), "IceCream : 80")