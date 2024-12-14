"""
Tests for models
"""

from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test Models."""

    def test_create_user_with_email_successful(self):
        """Test Creating a user with an email is successful."""
        email = 'mohab@example.com'
        password = "Mohab@123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_user_email_normalized(self):
        sample_emails = [
            ["test1@example.com", "test1@example.com"],
            ["test2@examPle.com", "test2@example.com"],
            ["Test3@EXamPle.com", "Test3@example.com"],
            ["Test4@EXAMPLE.COM", "Test4@example.com"],
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(
                email=email
            )
            self.assertEqual(user.email, expected)

    def test_create_user_without_email_raises_error(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('')

    def test_create_superUser_successfully(self):
        user = get_user_model().objects.create_superuser(
            email="Mohab@example.com"
        )

        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
