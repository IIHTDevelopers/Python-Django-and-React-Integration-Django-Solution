from django.test import TestCase
from django.urls import reverse
from library.test.TestUtils import TestUtils
from rest_framework.test import APITestCase
from django.test import TestCase
from rest_framework.test import APIClient


class RestaurantAPIFunctionalTest(TestCase):

    def test_create_menu_item(self):
        """Test if a menu item is created successfully via the API"""
        test_obj = TestUtils()
        try:
            # Setup API client
            client = APIClient()

            # Create a menu item through the API
            data = {'name': 'Burger', 'description': 'Beef burger', 'price': 5.99, 'category': 'Main Course'}
            response = client.post(reverse('menuitem-list'), data, format='json')

            # Verify if the menu item was created successfully
            self.assertEqual(response.status_code, 201)
            test_obj.yakshaAssert("TestCreateMenuItem", True, "functional")
            print("TestCreateMenuItem = Passed")
        except Exception as e:
            test_obj.yakshaAssert("TestCreateMenuItem", False, "functional")
            print(f"TestCreateMenuItem = Failed")