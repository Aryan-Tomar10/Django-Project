from django.test import TestCase
from django.urls import reverse

from .models import Post


class PostCreateTests(TestCase):
    def test_create_post_saves_and_redirects_to_detail(self):
        response = self.client.post(
            reverse("Post_new"),
            {"title": "Test post", "content": "Post content"},
        )

        post = Post.objects.get(title="Test post")
        self.assertEqual(post.content, "Post content")
        self.assertRedirects(response, reverse("Post_detail", args=[post.pk]))
