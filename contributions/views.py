from django.shortcuts import render
from django.http import *
from .models import Contributions

def fetch_pages(request):
  try:
    pages = []
    contributions = [i.get_json() for i in Contributions.objects.all()]
    for i in range(0, len(contributions), 3):
        pages.append(contributions[i: i + 3])
    if not pages:
      return JsonResponse([[]], safe=False)
    return JsonResponse(pages, safe=False)
  except Exception:
    return JsonResponse([], safe=False)