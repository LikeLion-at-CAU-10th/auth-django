from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
import json


def login_view(request):
    data = json.loads(request.body)
    username = data.get('username', None)
    password = data.get('password', None)

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        user_data = {
            "id": user.pk,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "is_active": user.is_active,
            "date_joined": user.date_joined,
            "last_login": user.last_login
        }
        return JsonResponse({"success": True, "message": "로그인 성공", "data": user_data}, status=200)
    else:
        return JsonResponse({"success": False, "message": "로그인 실패"}, status=403)


def logout_view(request):
    logout(request)
    return JsonResponse({"success": True, "message": "로그아웃 성공"}, status=200)
