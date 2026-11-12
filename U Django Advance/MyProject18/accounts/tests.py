from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class AuthenticationFlowTests(TestCase):
    def test_registration_creates_user_and_logs_them_in(self):
        response = self.client.post(
            reverse("register"),
            {
                "username": "new-user",
                "password1": "StrongPass!7293",
                "password2": "StrongPass!7293",
            },
        )

        self.assertRedirects(response, reverse("dashboard"))
        self.assertTrue(
            self.client.get(reverse("dashboard")).wsgi_request.user.is_authenticated
        )

    def test_login_authenticates_with_submitted_credentials(self):
        User.objects.create_user(username="existing-user", password="StrongPass!7293")

        response = self.client.post(
            reverse("login"),
            {"username": "existing-user", "password": "StrongPass!7293"},
        )

        self.assertRedirects(response, reverse("dashboard"))
        self.assertTrue(
            self.client.get(reverse("dashboard")).wsgi_request.user.is_authenticated
        )

    def test_registration_allows_multiple_users_without_email(self):
        for username in ("first-user", "second-user"):
            response = self.client.post(
                reverse("register"),
                {
                    "username": username,
                    "password1": "StrongPass!7293",
                    "password2": "StrongPass!7293",
                },
            )
            self.assertRedirects(response, reverse("dashboard"))

        self.assertEqual(User.objects.count(), 2)
