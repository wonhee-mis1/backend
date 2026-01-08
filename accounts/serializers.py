from django.contrib.auth import get_user_model
from rest_framework import serializers

from accounts.models import Profile

User = get_user_model()

class SingupSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True, min_length=4)
    nickname = serializers.CharField(max_length=30)

    def validate_username(self, data):
      if User.objects.filter(username=data).exists():
        raise serializers.ValidationError("User with this username already exists.")
      return data

    def create(self, validated_data):
      username = validated_data['username']
      password = validated_data['password']
      nickname = validated_data['nickname']

      user = User.objects.create_user(username=username, password=password)

      profile, _=Profile.objects.get_or_create(user=user)
      profile.nickname = nickname
      profile.save()

      return user