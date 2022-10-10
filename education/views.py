from django.http import *
from .models import Education

def fetch(request):
  try:
    return JsonResponse([i.get_json() for i in Education.objects.all()], safe=False)
  except Exception:
    return JsonResponse([], safe=False)