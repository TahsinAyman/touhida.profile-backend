from django.shortcuts import render
from django.http import *
from .models import ProfileCard

def fetch(request):
  try:
    profileCard = [i.get_json() for i in ProfileCard.objects.all()][0]
    return JsonResponse(profileCard)
  except Exception as e:
    return JsonResponse({})