import json
from django.db import models

class Achivements(models.Model):
  thumbnail = models.ImageField(upload_to="static/achivements")
  name = models.CharField(max_length=2000)
  date = models.CharField(max_length=2000)

  def __str__(self):
    return self.name

  def get_json(self):
    return {"thumbnail": str(self.thumbnail), "name": self.name, "date": self.date}