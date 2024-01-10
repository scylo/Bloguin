from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from blog.models import Post, Comment


class ApiViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.post = Post.objects.create(author=self.user, title='Test Post', content='Lorem ipsum')
        self.client = APIClient()

    def test_post_list_view(self):
        response = self.client.get(reverse('post-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_detail_view(self):
        post = Post.objects.create(author=self.user, title='Test Post', content='Lorem ipsum')
        response = self.client.get(reverse('post-view', args=[post.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_comment_list_view(self):
        response = self.client.get(reverse('comment-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_comment_detail_view(self):
        comment = Comment.objects.create(author=self.user, content='A comment', post=self.post)
        response = self.client.get(reverse('comment-view', args=[comment.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)