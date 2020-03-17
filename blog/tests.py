from django.test import TestCase, Client
from django.urls import reverse
from .models import Post, Category

class blogTestCate(TestCase):
    def setUp(self):
        client =  Client()
        category = Category.objects.create(title = 'Category 1',)
        post = Post.objects.create(title = 'Article 1', content= 'Mon Contenu', category_id = category, thumbnail_img = 'test.png')

    def test_blog_index(self):
        response = self.client.get(reverse('blog_index'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertContains(response, 'Article 1')
        self.assertContains(response, 'Mon Contenu')

    def test_show_category(self):
        response = self.client.get(reverse('show_category', kwargs={'slug': 'category-1'}))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'show_category.html')
    
    def test_show_post(self):
        response = self.client.get(reverse('show_post', kwargs={'slug': 'article-1'}))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'show_post.html')