import json
from django.db import models

class ProfileCard(models.Model):
  name = models.CharField(max_length=200)
  image = models.ImageField(upload_to="static/profileCard/")
  designation = models.CharField(max_length=2000)
  company = models.CharField(max_length=2000)

  def __str__(self):
    return self.name

  def get_json(self):
    return {"name": self.name, "image": str(self.image), "designation": self.designation, "company": self.company}