from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User
from django .shortcuts import reverse

class BlogPostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='user1')
        cls.post1 = Post.objects.create(
            title='Test title',
            text='Test text',
            status=Post.STATUS_CHOICES[0][0], # published
            author=cls.user,
        )
        cls.post2 = Post.objects.create(
            title='Test 2',
            text='lorem ipsum 2',
            status=Post.STATUS_CHOICES[1][0], # draft
            author=cls.user,
        )

    def test_post_model_str(self):
        post = self.post1
        self.assertEqual(str(post), post.title)

    def test_post_detail(self):
        self.assertEqual(self.post1, 'post1')

    def test_post_list_url(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_post_lost_url_by_name(self):
        response = self.client.get(reverse('posts_list'))
        self.assertEqual(response.status_code, 200)

    def test_post_title_on_blog_list_page(self):
        response = self.client.get(reverse('posts_list'))
        self.assertContains(response, 'Test title')

    def test_post_detail_url(self):
        response = self.client.get('/blog/1/')
        self.assertEqual(response.status_code, 200)

    def test_post_detail_url_by_name(self):
        response = self.client.get(reverse('post_detail', args=[self.post1.id]))
        self.assertEqual(response.status_code, 200)

    def test_post_details_on_blog_detail_page(self):
        response = self.client.get(reverse('post_detail', args=[self.post1.id]))
        self.assertContains(response, self.post1.title)
        self.assertContains(response, self.post1.text)

    def test_status_404_if_post_id_not_found(self):
        response = self.client.get(reverse('post_detail', args=[100]))
        self.assertEqual(response.status_code, 404)

    def test_draft_post_not_show_in_posts_list(self):
        response = self.client.get(reverse('posts_list'))
        self.assertContains(response, self.post1.title)
        self.assertNotContains(response, self.post2.title)

    def test_post_create_view(self):
        response = self.client.post(reverse('post_create'), {
            'title': 'Test title',
            'text': 'Test text',
            'status': 'published',
            'author': self.user.id
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, 'Test title')
        self.assertEqual(Post.objects.last().text, 'Test text')