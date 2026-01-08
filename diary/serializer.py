from rest_framework import serializers

from diary.models import DiaryEntry


class DiaryEntrySerializer(serializers.ModelSerializer):
  entry_date =serializers.DateField(read_only=True)
  user = serializers.HiddenField(default=serializers.CurrentUserDefault())
  class Meta:
    model = DiaryEntry
    fields = ["id", "entry_date", "content", "user"]