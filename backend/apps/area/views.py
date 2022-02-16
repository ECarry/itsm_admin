from rest_framework.views import APIView, Response
from rest_framework import status
from .models import Area
from .serializers import AreaSerializers, AreaDetailSerializers


# 所有省份列表试图
class ProvinceListView(APIView):
    def get(self, request):
        # 查询全省
        province = Area.objects.filter(parent=None)

        # 序列化
        serializer = AreaSerializers(province, many=True)

        # 返回数据
        return Response(serializer.data)


# 省份所有下级市
class ProvinceDetailListView(APIView):
    def get(self, request, pk):
        # 某省下的市
        try:
            province_detail = Area.objects.get(id=pk)
        except Area.DoesNotExist:
            return Response({'message': '查无省份'}, status=status.HTTP_400_BAD_REQUEST)

        # 序列化器
        serializer = AreaDetailSerializers(province_detail)

        # 返回数据
        return Response(serializer.data)






