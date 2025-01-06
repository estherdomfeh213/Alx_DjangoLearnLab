from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
# Create your tests here.


class AuthTests(TestCase):
    def test_registration(self):
        response = self.client.post(reverse('blog:register'), {
            'username': 'testuser',
            'password1': 'password123',
            'password2': 'password123'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_login(self):
        User.objects.create_user(username='testuser', password='password123')
        response = self.client.post(reverse('blog:login'), {
            'username': 'testuser',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.assertTrue('_auth_user_id' in self.client.session)

    def test_logout(self):
        User.objects.create_user(username='testuser', password='password123')
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('blog:logout'))
        self.assertEqual(response.status_code, 302)  # Redirect after logout

    def test_profile_access_without_login(self):
        response = self.client.get(reverse('blog:profile'))
        self.assertEqual(response.status_code, 302)  # Redirect to login page
        self.assertTrue(response.url.startswith(reverse('blog:login')))
