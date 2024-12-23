from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status
from .models import Book 

class BookAPITests(APITestCase):
    def setUp(self):
        #  Test user for authentication
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.client.login(username="testuser", password="testpassword")  # Login using the test user

    def test_create_book(self):
        # Test for creating a book
        data = {
            "title": "Test Book",
            "author": "Test Author",
            "publication_year": 2023
        }
        response = self.client.post("/api/books/", data, format="json")
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "Test Book")
        self.assertEqual(response.data["author"], "Test Author")
        self.assertEqual(response.data["publication_year"], 2023)
