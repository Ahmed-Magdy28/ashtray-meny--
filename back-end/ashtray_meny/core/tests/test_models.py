"""
Test For Models
"""
from django.core.exceptions import ValidationError
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test Models."""

    def test_create_user_with_email_successful(self):
        """Test Creating a User with an Email is Successful"""

        email = 'test@example.com'
        password = "TestPassword123$"
        username = "test"
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
            username=username
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_superuser(self):
        """Test creating super user"""
        user = get_user_model().objects.create_superuser(
            email='test@example.com',
            password="TestPassword123$",
            username="test"
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
