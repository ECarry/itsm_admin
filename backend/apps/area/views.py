from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.views import APIView, Response
from rest_framework import status
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Area
from .serializers import AreaSerializers, AreaDetailSerializers

# 88集
# v1
# 所有省份列表试图
# class AreaListView(APIView):
#     def get(self, request):
#         # 查询全省
#         province = Area.objects.filter(parent=None)
#
#         # 序列化
#         serializer = AreaSerializers(province, many=True)
#
#         # 返回数据
#         return Response(serializer.data)
# v2
# class AreaListView(GenericAPIView):
#     queryset = Area.objects.filter(parent=None)
#     serializer_class = AreaSerializers
#
#     def get(self, request):
#         area = self.get_queryset()
#         serializer = self.get_serializer(area, many=True)
#
#         return Response(serializer.data)
# v3
# class AreaListView(ListModelMixin, GenericAPIView):
#     queryset = Area.objects.filter(parent=None)
#     serializer_class = AreaSerializers
#
#     def get(self, request):
#         return self.list(request)
# v4
# class AreaListView(ListAPIView):
#     queryset = Area.objects.filter(parent=None)
#     serializer_class = AreaSerializers


# v1
# 省所有下级市
# 市下所有区县
# class AreaDetailListView(APIView):
#     def get(self, request, pk):
#         try:
#             area_detail = Area.objects.get(id=pk)
#         except Area.DoesNotExist:
#             return Response({'message': '查无此地区'}, status=status.HTTP_400_BAD_REQUEST)
#
#         # 序列化器
#         serializer = AreaDetailSerializers(area_detail)
#
#         # 返回数据
#         return Response(serializer.data)
# v2
# class AreaDetailListView(RetrieveAPIView):
#     serializer_class = AreaDetailSerializers
#     queryset = Area.objects.all()

class AreaViewSet(ReadOnlyModelViewSet):
    # 指定查询集
    def get_queryset(self):
        if self.action == 'list':
            return Area.objects.filter(parent=None)
        else:
            return Area.objects.all()

    # 指定序列化器
    def get_serializer_class(self):
        if self.action == 'list':
            return AreaSerializers
        else:
            return AreaDetailSerializers
