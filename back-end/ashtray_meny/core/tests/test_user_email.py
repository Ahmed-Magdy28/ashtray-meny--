"""a tests for the emails for the user"""
from django.core.exceptions import ValidationError
from django.test import TestCase
from django.contrib.auth import get_user_model


class EmailTests(TestCase):
    """Test User Emails."""

    def test_new_user_email_normalized(self):
        """Test email normalized for new users"""
        sample_emails = [
            ["test1@EXAMPLE.com", "test1@example.com"],
            ["Test2@EXAMPLE.com", "Test2@example.com"],
            ["TEST3@Example.com", "TEST3@example.com"],
            ["test4@example.COM", "test4@example.com"],
        ]
        for i, (email, expected) in enumerate(sample_emails):
            user = get_user_model().objects.create_user(
                email=email,
                password='Sample123$',
                username=f'test{i}'  # Ensure a unique name for each user
            )
            self.assertEqual(user.email, expected)

    def test_create_user_without_email_raises_error(self):
        """Test that creating a user without an email raises an error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email='',
                password="TestPassword123!",
                username="test"
            )

    # def test_create_user_with_existing_email_raises_error(self):
    #     """Test that creating a user with an existing email raises an error."""
    #     email = "test@example.com"
    #     password = "ValidPassword123$"
    #     username1 = "unique_username1"
    #     username2 = "unique_username2"  # Change username to ensure uniqueness

    #     # Create the first user
    #     get_user_model().objects.create_user(
    #         email=email,
    #         password=password,
    #         username=username1
    #     )

    #     # Try to create a second user with the same email
    #     with self.assertRaises(ValueError):
    #         get_user_model().objects.create_user(
    #             email=email,  # Same email as the first user
    #             password="AnotherValidPassword123$",
    #             username=username2  # Ensure unique username
    #         )

    def test_create_user_with_empty_email_raises_error(self):
        """Test that creating a user with an empty email raises an error."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=None,  # Empty email
                password="ValidPassword123$",
                username="valid_username"
            )
