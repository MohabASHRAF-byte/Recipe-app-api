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

    def test_create_user_already_exists_error(self):
        """Test create user already exists error."""
        payload = {
            'email': 'test1@example.com',
            'password': 'testPass123',
            'name': 'test1',
        }
        create_user(**payload)

        response = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_password_too_short(self):
        """Test create user password too short."""
        payload = {
            'email': 'test1@example.com',
            'password': 'te',
            'name': 'test1',
        }

        response = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        uses_exists = get_user_model().objects.filter(
            email=payload['email']
        ).exists()
        self.assertFalse(uses_exists)
