from django.db import models

class Education(models.Model):
  degree = models.CharField(max_length=2000)
  institute = models.CharField(max_length=2000)
  awardingBody = models.CharField(max_length=2000)
  passingYear = models.IntegerField()

  def __str__(self):
    return self.degree

  def get_json(self):
    return {"degree": self.degree, "institute": self.institute, "awardingBody": self.awardingBody, "passingYear": self.passingYear}