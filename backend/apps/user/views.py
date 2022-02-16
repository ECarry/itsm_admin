from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework import status
from rest_framework.views import APIView, Response
from .serializers import CreateUserSerializers, MyTokenObtainPairSerializer, UserDetailSerializers
from .models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import permissions


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


# 验证注册用户名是否存在
class VerifyUsernameCount(APIView):
    def get(self, request, username):
        count = User.objects.filter(username=username).count()

        data = {
            'username': username,
            'count': count
        }

        return Response(data)


# 自定义令牌
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# 个人信息详情
class UserDetailView(RetrieveAPIView):
    serializer_class = UserDetailSerializers

    # 设置需要认证才能获取信息
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user


