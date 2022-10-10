from django.http import JsonResponse
from django.shortcuts import render
from .models import Photos

def fetch_pages(request):
  try:
    pages = []
    photos = [i.get_json() for i in Photos.objects.all()]
    for i in range(0, len(photos), 4):
        pages.append(photos[i: i + 4])
    if not photos:
      return JsonResponse([[]], safe=False)
    return JsonResponse(pages, safe=False)
  except Exception:
    return JsonResponse([[]], safe=False)