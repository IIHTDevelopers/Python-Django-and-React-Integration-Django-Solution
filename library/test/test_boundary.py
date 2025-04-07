from rest_framework.test import APITestCase
from library.test.TestUtils import TestUtils
from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APITestCase
from library.models import MenuItem, Order
from rest_framework.test import APIClient


class RestaurantAPIBoundaryTest(TestCase):
    def test_maximum_menu_items(self):
        """Test if the maximum number of menu items can be added"""
        test_obj = TestUtils()
        try:
            max_items = 100  # Hypothetical boundary limit
            client = APIClient()
            for i in range(max_items):
                data = {'name': f'Item {i}', 'description': f'Description for item {i}', 'price': 10.0, 'category': 'Main Course'}
                client.post(reverse('menuitem-list'), data, format='json')
            
            # Verify if the limit is reached without any issues
            self.assertEqual(MenuItem.objects.count(), max_items)
            test_obj.yakshaAssert("TestMaxMenuItems", True, "boundary")
            print("TestMaxMenuItems = Passed")
        except Exception as e:
            test_obj.yakshaAssert("TestMaxMenuItems", False, "boundary")
            print(f"TestMaxMenuItems = Failed")
