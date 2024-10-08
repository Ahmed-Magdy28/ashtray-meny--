"""Database Models """
from re import search
from venv import create
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionManager, PermissionsMixin)


def validate_password_strength(password):
    """Validate password meets required complexity."""
    if len(password) < 8:
        raise ValidationError("Password must be at least 8 characters long.")
    if not search(r'[A-Z]', password):
        raise ValidationError(
            "Password must contain at least 1 uppercase letter.")
    if not search(r'[a-z]', password):
        raise ValidationError(
            "Password must contain at least 1 lowercase letter.")
    if not search(r'[0-9]', password):
        raise ValidationError("Password must contain at least 1 digit.")
    if not search(r'[!@#$%^&*(),.?":{}|<>]', password):
        raise ValidationError(
            "Password must contain at least 1 special character.")
    return password


class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, password, username, **extra_fields):
        """Create a User & Save & Return User"""
        # check if the email is empty
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have an Unique username")
        # check if password is empty
        if not password:
            raise ValueError("Users must have a password")

        # create the user
        user = self.model(email=self.normalize_email(email),
                          username=username, **extra_fields)

        # Validate password strength
        validate_password_strength(password)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        """Create a SuperUser & Save & Return SuperUser"""
        user = self.create_user(
            email=email, username=username, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system"""
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # Add username to the required fields
