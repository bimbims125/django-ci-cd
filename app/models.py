from django.db import models

# Create your models here.
class Blogs(models.Model):
  title = models.CharField(max_length=255, null=False)
  description = models.TextField()
  author = models.CharField(max_length=40, null=False)

  def __str__(self) -> str:
    return self.title
