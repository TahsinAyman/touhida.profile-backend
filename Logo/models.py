from django.db import models

class Logo(models.Model):
    logo = models.ImageField(upload_to="static/logo/")

    def get_json(self):
        return {"logo": str(self.logo)}