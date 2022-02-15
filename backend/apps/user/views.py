from rest_framework.generics import CreateAPIView
from rest_framework import status
from rest_framework.views import APIView, Response
from .serializers import CreateUserSerializers
from .models import User


# 注册视图
class CreateUserView(CreateAPIView):
    serializer_class = CreateUserSerializers


# 验证邮箱是否存在
class VerifyEmailCount(APIView):
    def get(self, request, email):
        count = User.objects.filter(email=email).count()

        data = {
            'email': email,
            'count': count
        }
        return Response(data)
