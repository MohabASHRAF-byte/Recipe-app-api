"""Test django admin site"""

from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase, Client


class AdminSiteTests(TestCase):
    """Test admin site"""

    def setUp(self):
        self.client = Client()
        admin = get_user_model().objects.create_superuser(
            email='admin@example.com',
            password='testpass123'
        )
        self.client.force_login(admin)

        self.user = get_user_model().objects.create_user(
            name='Mohab',
            email='user@example.com',
            password='testpass123'
        )

    def test_users_list(self):
        """Test that users are listed"""
        url = reverse('admin:core_user_changelist')
        response = self.client.get(url)

        self.assertContains(response, self.user.name)
        self.assertContains(response, self.user.email)
