from django.db import models

class Title(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    def get_json(self):
        return {"title": self.title}