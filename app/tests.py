from django.test import TestCase
from app.models import Blogs

# Create your tests here.

class PostTest(TestCase):

  def setUp(self):
    self.blog = Blogs.objects.create(title="Test", description="Test CI/CD", author="Test Jeri")
    # print(self.blog)
  def test_blog_post(self):
    d = self.blog
    self.assertTrue(isinstance(d, Blogs))
    self.assertEqual(str(d), "Test")

