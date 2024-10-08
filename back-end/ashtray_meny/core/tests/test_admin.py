"""Tests for Django Admin Modification."""
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):
    """Tests for Django admin"""

    def setUp(self):
        """Create User and Client."""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email="TestAdmin@example.com",
            password="Hello950!@",
            username="TestAdmin"
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email="TestUser@example.com",
            password="Hello928!",
            username="HEllo User"
        )

    def test_users_list(self):
        """Test that Users are listed on page"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.username)
        self.assertContains(res, self.user.email)

    def test_edit_user_page(self):
        """Test the edit page works or not"""
        url = reverse('admin:core_user_change', args=[self.user.pk])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test the create user page works."""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
