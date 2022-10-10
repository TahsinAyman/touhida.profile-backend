import re
from statistics import mode
from django.db import models

class Comments(models.Model):
  message = models.TextField(max_length=2000)
  name = models.CharField(max_length=2000)
  designation = models.CharField(max_length=2000)
  photo = models.ImageField(upload_to="static/comments/")

  def __str__(self):
    return self.name

  def get_json(self):
    return {"name": self.name, "message": self.message, "designation": self.designation, "photo": str(self.photo)}