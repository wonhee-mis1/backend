from django.urls import path
from .api import SignupAPIView

urlpatterns = [
  path('signup/', SignupAPIView.as_view()),
]