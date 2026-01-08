from django.core.serializers import serialize
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.serializers import SingupSerializer


class SignupAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
      serializer = SingupSerializer(data=request.data)
      serializer.is_valid(raise_exception=True)
      user = serializer.save()
      return Response({"message": "ok", "user_id": user.id}, status=status.HTTP_201_CREATED)