"""a tests for the username for the users"""
from django.core.exceptions import ValidationError
from django.test import TestCase
from django.contrib.auth import get_user_model


class PasswordTests(TestCase):
    """Test User Password."""

    def test_create_user_without_username_raises_error(self):
        """Test that creating a user without an username raises an error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email="test@example.com",
                password="TestPassword123!",
                username=None  # type: ignore
            )

    # def test_create_user_with_existing_username_raises_error(self):
    #     """Test that creating a user with an existing username raises an error."""
    #     username = "testuser"
    #     email1 = "user1@example.com"
    #     email2 = "user2@example.com"  # Different email for the second user
    #     password = "ValidPassword123$"

    #     get_user_model().objects.create_user(
    #         email=email1,
    #         password=password,
    #         username=username
    #     )

    #     with self.assertRaises(ValueError):
    #         get_user_model().objects.create_user(
    #             email=email2,
    #             password=password,
    #             username=username  # This username already exists
    #         )

    def test_create_user_with_unique_username_successful(self):
        """Test creating a user with a unique username is successful"""
        email = "uniqueuser@example.com"
        password = "ValidPassword123$"
        username = "unique_username"

        user = get_user_model().objects.create_user(
            email=email,
            password=password,
            username=username
        )

        self.assertEqual(user.username, username)

    def test_create_user_with_empty_username_raises_error(self):
        """Test that creating a user with an empty username raises an error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email="test@example.com",
                password="TestPassword123!",
                username=""  # Empty username
            )
