from django.db import models

# Create your models here.

class User(models.Model):
  first_name = models.CharField(max_length=264)
  last_name = models.CharField(max_length=264)
  email = models.CharField(max_length=264) # Deberia de ser unique unique=True

  def __str__(self):
    return self.first_name + ' ' + self.last_name
