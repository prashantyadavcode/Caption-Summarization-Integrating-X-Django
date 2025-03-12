from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def home_view(request):
    return JsonResponse({"message": "Welcome to Caption Summarization API!"})

urlpatterns = [
    path("", home_view, name="home"), 
    path("admin/", admin.site.urls),
    path("summarizer/", include("summarizer.urls")),
]