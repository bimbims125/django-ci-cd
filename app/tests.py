from django.test import TestCase

# Create your tests here.

class IncrementTest(TestCase):

  def test_add(self):
    result = 4 + 5
    self.assertEqual(result, 9)

  def test_subst(self):
    result = 20 - 19
    self.assertEqual(result, 1)
