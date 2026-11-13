from django.core import mail
from django.test import TestCase, override_settings
from django.urls import reverse


class SendTestEmailTests(TestCase):
    @override_settings(
        EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend',
        DEFAULT_FROM_EMAIL='sender@example.com',
    )
    def test_email_route_sends_message(self):
        response = self.client.get(reverse('send_test_email'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].from_email, 'sender@example.com')
