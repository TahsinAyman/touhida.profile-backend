from django.http import JsonResponse
from .models import Logo

def fetch(request):
    try:
        logo = [i.get_json() for i in Logo.objects.all()][0]
        return JsonResponse(logo)
    except Exception:
        return JsonResponse({})