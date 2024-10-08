"""a tests for the Passwords for the users"""
from django.core.exceptions import ValidationError
from django.test import TestCase
from django.contrib.auth import get_user_model


class PasswordTests(TestCase):
    """Test User Password."""

    def test_create_user_without_password_raises_error(self):
        """Test that creating a user without a password raises an error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email="test@example.com",
                password=None,
                username="test"
            )  # type: ignore

    def test_create_user_with_short_password(self):
        """Test creating a user with a short password raises a validation error"""
        email = "test@example.com"
        short_password = "Ab1!"  # too short

        with self.assertRaises(ValidationError):
            get_user_model().objects.create_user(
                email=email,
                password=short_password,
                username="test"
            )

    def test_create_user_with_no_uppercase_password(self):
        """Test creating a user with no uppercase letter raises a validation error"""
        email = "test@example.com"
        password_no_uppercase = "testpassword123!"

        with self.assertRaises(ValidationError):
            get_user_model().objects.create_user(
                email=email,
                password=password_no_uppercase,
                username="test"
            )

    def test_create_user_with_no_lowercase_password(self):
        """Test creating a user with no lowercase letter raises a validation error"""
        email = "test@example.com"
        password_no_lowercase = "TESTPASSWORD123!"

        with self.assertRaises(ValidationError):
            get_user_model().objects.create_user(
                email=email,
                password=password_no_lowercase,
                username="test"
            )

    def test_create_user_with_no_digit_password(self):
        """Test creating a user with no digit raises a validation error"""
        email = "test@example.com"
        password_no_digit = "TestPassword!"

        with self.assertRaises(ValidationError):
            get_user_model().objects.create_user(
                email=email,
                password=password_no_digit,
                username="test"
            )

    def test_create_user_with_no_special_character_password(self):
        """Test creating a user with no special character raises a validation error"""
        email = "test@example.com"
        password_no_special_char = "TestPassword123"

        with self.assertRaises(ValidationError):
            get_user_model().objects.create_user(
                email=email,
                password=password_no_special_char,
                username="test"
            )
