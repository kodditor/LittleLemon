from django.test import TestCase
from .models import menu

class MenuTest(TestCase):
    def test_menu(self):
        self.item = menu.objects.create(id=99, title="IceCream", price=80, inventory=100)
        self.assertEqual(self.item.__str__(), "IceCream : 80")

class MenuViewTest(TestCase):
    def setUp(self):
        self.item_1 = menu.objects.create(id=99, title="IceCream", price=80, inventory=100)
        self.item_2 = menu.objects.create(id=100, title="Biscuits", price=60, inventory=10)
        self.item_3 = menu.objects.create(id=101, title="Fish", price=40, inventory=70)
    
    def test_getall(self):
        
        expected_values = ['IceCream : 80','Biscuits : 60', 'Fish : 40']
        test_values = [self.item_1, self.item_2, self.item_3 ]

        for idx, value in enumerate(test_values):
            self.assertEqual(value.__str__(), expected_values[idx])
