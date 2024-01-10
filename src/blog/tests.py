from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Post, Comment

# Create your tests here.
class BlogViewsTest(TestCase):
    fixtures = ['test_data.json']

    def setUp(self):
        self.client = Client()

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_add_post_view(self):
        user = User.objects.first()
        response = self.client.post(
            reverse('add_post'), 
            {
                'title': 'New Post',
                'content': 'Some content',
                'author': user.id
            }
        )
        self.assertEqual(response.status_code, 302)