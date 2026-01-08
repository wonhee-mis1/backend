import json
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

User = get_user_model()

def _json(request):
  try:
    return json.loads(request.body.decode())
  except:
    return {}

@csrf_exempt
def signup(request):
  if request.method != 'POST':
    return JsonResponse({'message': 'Method not allowed'}, status=405)

  data = _json(request)
  username = data.get('username')
  password = data.get('password')
  nickname = data.get('nickname')

  if not username or not password or not nickname:
    return JsonResponse({'message': "username, password, nickname are required"}, status=400)

  if User.objects.filter(username=username).exists():
    return JsonResponse({'message': 'username already exists'}, status=409)

  user = User.objects.create_user(username=username, password=password)
  user.profile.nickname = nickname
  user.profile.save()

  return JsonResponse({'message': 'ok', 'user_id': user.id}, status=200)