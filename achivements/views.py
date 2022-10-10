from django.http import *
from .models import Achivements

def fetch_pages(request):
  try:
    pages = []
    achivements = [i.get_json() for i in Achivements.objects.all()]
    for i in range(0, len(achivements), 3):
        pages.append(achivements[i: i + 3])
    if not pages:
      return JsonResponse([[]], safe=False)
    return JsonResponse(pages, safe=False)
  except Exception:
    return JsonResponse([[]], safe=False)