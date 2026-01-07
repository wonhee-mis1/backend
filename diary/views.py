import json
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .models import DiaryEntry
from datetime import date

user = User.objects.first()

@csrf_exempt
@require_POST
def post_diary(request):
    data = json.loads(request.body)

    entry = DiaryEntry.objects.create(
        user=user,
        entry_date=data.get("entry_date", date.today()),
        content=data["content"]
    )

    return JsonResponse({
        "id": entry.id,
        "message": "작성 완료되었습니다"
    })
