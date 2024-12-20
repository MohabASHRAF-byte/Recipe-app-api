"""
Tests for the user API.
"""
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework import status

CREATE_USER_URL = reverse('user:create')


def create_user(**params):
    """Create and return new user."""
    return get_user_model().objects.create_user(**params)


class PublicUserTest(TestCase):
    """Tset the public features of the user API."""

    def setUp(self):
        self.client = APIClient()

    def test_create_user_success(self):
        """Test create user success."""
        payload = {
            'email': 'test1@example.com',
            'password': 'testPass123',
            'name': 'test1',
        }

        response = self.client.post(CREATE_USER_URL, payload)  # noqa: E231

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        user = get_user_model().objects.get(
            email=payload['email']
        )
        self.assertTrue(user.check_password(payload['password']))

        self.assertNotIn('password', response.data)
