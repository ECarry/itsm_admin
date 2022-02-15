from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from .serializers import CreateUserSerializers


class UserView(CreateAPIView):
    serializer_class = CreateUserSerializers
