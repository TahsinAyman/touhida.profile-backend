import json
from django.db import models


class Content(models.Model):
  id = models.AutoField(primary_key=True)
  title = models.CharField(max_length=200)
  description = models.TextField(max_length=2000)
  thumbnail = models.ImageField(upload_to="static/content/")
  link = models.URLField(max_length=20000)

  def __str__(self):
    return self.title

  def get_json(self):
    return {"id": self.id, 
    "title": self.title, 
    "description": self.description, 
    "thumbnail": str(self.thumbnail), 
    "link": self.link}
