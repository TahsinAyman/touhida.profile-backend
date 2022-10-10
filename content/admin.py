from django.contrib import admin
from . import models

admin.site.site_header = "Touhida Akter"
admin.site.register(models.Content)