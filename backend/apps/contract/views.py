from rest_framework.views import APIView, Response
from rest_framework.generics import CreateAPIView
from rest_framework import status
from .serializers import ContractSerializers
from .models import Contract


# 合同列表
class ContractListView(APIView):
    def get(self, request):
        # 所有合同
        contracts = Contract.objects.all()

        # 序列化
        serializer = ContractSerializers(contracts, many=True)

        # 返回数据
        return Response(serializer.data, status=status.HTTP_200_OK)


# 创建合同
class CreateContractView(CreateAPIView):
    serializer_class = ContractSerializers

