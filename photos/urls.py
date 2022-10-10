from django.urls import path
from . import views

urlpatterns = [
  path('fetch/pages/', views.fetch_pages)
]