from django.contrib import admin
from . import models

admin.site.site_header = "Site Administration"
admin.site.register(models.Content)