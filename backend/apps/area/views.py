from rest_framework.views import APIView, Response
from rest_framework import status
from .models import Area
from .serializers import AreaSerializers, AreaDetailSerializers


# 所有省份列表试图
class AreaListView(APIView):
    def get(self, request):
        # 查询全省
        province = Area.objects.filter(parent=None)

        # 序列化
        serializer = AreaSerializers(province, many=True)

        # 返回数据
        return Response(serializer.data)


# 省所有下级市
# 市下所有区县
class AreaDetailListView(APIView):
    def get(self, request, pk):
        try:
            area_detail = Area.objects.get(id=pk)
        except Area.DoesNotExist:
            return Response({'message': '查无此地区'}, status=status.HTTP_400_BAD_REQUEST)

        # 序列化器
        serializer = AreaDetailSerializers(area_detail)

        # 返回数据
        return Response(serializer.data)






