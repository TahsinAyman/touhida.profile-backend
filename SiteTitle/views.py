from django.http import JsonResponse
from .models import Title

def fetch(request):
    try:
        title = [i.get_json() for i in Title.objects.all()][0]
        return JsonResponse(title)
    except Exception:
        return JsonResponse({"title": "Profile"})
    