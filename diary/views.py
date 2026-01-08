from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import DiaryEntry
from .serializer import DiaryEntrySerializer


class DiaryEntryAPIView(APIView):
  def get(self, request):
    user = User.objects.first()
    queryset = DiaryEntry.objects.filter(user=user).order_by("-entry_date")
    serializer = DiaryEntrySerializer(queryset, many=True)
    return Response(serializer.data)

  def post(self, request):
    serializer = DiaryEntrySerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
      serializer.save(user=User.objects.first())
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)