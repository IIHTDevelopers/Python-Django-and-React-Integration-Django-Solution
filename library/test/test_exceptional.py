from rest_framework.test import APITestCase
from django.db import IntegrityError
from library.test.TestUtils import TestUtils
from django.urls import reverse
from unittest.mock import patch
from django.urls import get_resolver
from django.test import TestCase
from library.models import MenuItem, Order
from rest_framework.test import APIClient


class RestaurantAPIExceptionalTest(TestCase):

    def test_invalid_order_status_update(self):
        """Test if updating order status with an invalid value raises a proper exception"""
        test_obj = TestUtils()
        try:
            # Setup API client
            client = APIClient()

            # Create a menu item and an order
            menu_item = MenuItem.objects.create(name='Pizza', description='Delicious pizza', price=8.99, category='Main Course')
            order = Order.objects.create(customer_name='John Doe')
            order.menu_items.add(menu_item)

            # Trying to update the order with an invalid status
            invalid_status = {'status': 'not_a_valid_status'}
            response = client.patch(reverse('order-update-status', kwargs={'pk': order.id}), invalid_status, format='json')

            # Check if proper error is returned
            self.assertEqual(response.status_code, 400)
            test_obj.yakshaAssert("TestInvalidOrderStatusUpdate", True, "exceptional")
            print("TestInvalidOrderStatusUpdate = Passed")
        except Exception as e:
            test_obj.yakshaAssert("TestInvalidOrderStatusUpdate", False, "exceptional")
            print(f"TestInvalidOrderStatusUpdate = Failed")
