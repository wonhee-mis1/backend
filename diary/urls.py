from django.urls import path

from .views import DiaryEntryAPIView

urlpatterns = [
    path("", DiaryEntryAPIView.as_view()),
]
