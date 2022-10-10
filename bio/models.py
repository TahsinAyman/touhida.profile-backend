from django.db import models


class Bio(models.Model):
    name = models.CharField(max_length=3000)
    description = models.TextField(max_length=99999)

    def __str__(self):
        return self.name

    def get_json(self):
        return {
            "name": self.name,
            "description": self.description,
        }
