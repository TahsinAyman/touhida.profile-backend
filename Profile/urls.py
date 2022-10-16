"""Profile URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve 
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('api/v1/contents/', include("content.urls")),
    path('api/v1/contributions/', include("contributions.urls")),
    path('api/v1/photos/', include("photos.urls")),
    path('api/v1/profileCard/', include("profileCard.urls")),
    path('api/v1/education/', include("education.urls")),
    path('api/v1/achivements/', include("achivements.urls")),
    path('api/v1/comments/', include("comments.urls")),
    path('api/v1/bio/', include("bio.urls")),
    path('api/v1/title/', include("SiteTitle.urls")),
    path('api/v1/logo/', include("Logo.urls")),

    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]
