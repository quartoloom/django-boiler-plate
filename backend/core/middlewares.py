import jwt
from django.conf import settings
from accounts.models import User
from django.http import JsonResponse
from django.forms import ValidationError


class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        token = request.headers.get("Authorization")
        if request.path.startswith("/api"):
            if not token:
                return JsonResponse(data={"msg": "Token not provided"}, status=403)
            try:
                jwt_data = jwt.decode(token, settings.JWT_SECRET, algorithms=["HS256"])
                request.this_user = User.objects.get(id=jwt_data.get("user_id"))
                request.this_user_type = jwt_data.get("user_type")
                
                response = self.get_response(request)
                return response
            except (jwt.exceptions.InvalidSignatureError, User.DoesNotExist):
                return JsonResponse(data={"msg": "Invalid token"}, status=401)
        response = self.get_response(request)
        return response
