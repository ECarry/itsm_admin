from django.http import Http404
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView, Response
from rest_framework.generics import CreateAPIView
from rest_framework import status, generics
from .serializers import ContractSerializers
from .models import Contract
from django.db.models import Q
import time

# # 分页器
# class StandardResultsSetPagination(PageNumberPagination):
#     page_size = 10
#     page_size_query_param = 'page_size'
#     max_page_size = 1000


# 合同列表
class ContractList(generics.ListAPIView):
    # 所有合同
    queryset = Contract.objects.all()

    # 序列化
    serializer_class = ContractSerializers

    # # 分页器
    # pagination_class = StandardResultsSetPagination


# 创建合同
class ContractCreate(CreateAPIView):
    serializer_class = ContractSerializers


# 合同详情
class ContractDetail(APIView):
    def get_object(self, pk):
        try:
            return Contract.objects.get(pk=pk)
        except Contract.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        contract = self.get_object(pk)
        serializer = ContractSerializers(contract)
        return Response(serializer.data)

    def delete(self, request, pk):
        contract = self.get_object(pk)
        contract.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# 合同搜索
class ContractSearch(APIView):
    def get(self, request, string):
        contracts = Contract.objects.filter(Q(area__contains=string) | Q(project_num__contains=string)
                                            | Q(custom__contains=string))

        if contracts.count() == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializers = ContractSerializers(contracts, many=True)

        return Response(serializers.data)
