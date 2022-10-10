from .models import Comments
from django.http import JsonResponse

def fetch(request):
  try:
    comments = [i.get_json() for i in Comments.objects.all()]
    return JsonResponse(comments, safe=False)
  except Exception:
    return JsonResponse([], safe=False)