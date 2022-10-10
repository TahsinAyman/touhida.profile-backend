import json
from django.db import models

class Contributions(models.Model):
  headline = models.CharField(max_length=2000)
  description = models.TextField(max_length=20000)

  def __str__(self):
    return self.headline

  def get_json(self):
    return {"headline": self.headline, "description": self.description}