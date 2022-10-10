from django.http import *
from .models import Bio

def fetch(request):
  try:
    bio = (Bio.objects.all()[0]).get_json();
    return JsonResponse(bio, safe=False)
  except Exception:
    return JsonResponse([], safe=False)  
