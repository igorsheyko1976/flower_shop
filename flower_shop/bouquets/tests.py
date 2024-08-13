from django.test import TestCase
from .models import Bouquet, Order
from django.contrib.auth.models import User

class BouquetModelTest(TestCase):
    def test_bouquet_creation(self):
        bouquet = Bouquet.objects.create(
            name="Розы",
            description="Красивые красные розы",
            price=1500.00
        )
        self.assertEqual(bouquet.name, "Розы")

class OrderModelTest(TestCase):
    def test_order_creation(self):
        user = User.objects.create_user(username="testuser", password="password")
        bouquet = Bouquet.objects.create(name="Розы", price=1500.00)
        order = Order.objects.create(
            user=user,
            bouquet=bouquet,
            delivery_address="ул. Цветочная, д. 5",
            delivery_date="2023-08-11 12:00"
        )
        self.assertEqual(order.user.username, "testuser")
