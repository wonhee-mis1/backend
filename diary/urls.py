from django.http import JsonResponse
from django.urls import path
from . import views

urlpatterns = [
    path('', lambda request: JsonResponse({"message": "diary api"})),
    path('post/', views.post_diary),
]
