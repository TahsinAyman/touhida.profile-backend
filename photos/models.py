import json
from django.db import models

class Photos(models.Model):
  img = models.ImageField(upload_to="static/images/")

  def get_json(self):
    return {"img": str(self.img)}