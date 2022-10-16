from django.http import *
from .models import Content

def fetch_pages(request):
  try:
    pages = []
    content = [i.get_json() for i in Content.objects.all()]
    for i in range(0, len(content), 3):
        pages.append(content[i: i + 3])
    if not pages:
        return JsonResponse([[]], safe=False)
    return JsonResponse(pages, safe=False)
  except Exception:
    return JsonResponse([[]], safe=False)

def fetch(request):
  try:
    id = request.GET.get("id")
    if not id:
      return JsonResponse([i.get_json() for i in Content.objects.all()], safe=False)
    else:
      return JsonResponse((Content.objects.get(id=id)).get_json(), safe=False)
  except Exception as e:
    print(e)
    return JsonResponse([], safe=False)