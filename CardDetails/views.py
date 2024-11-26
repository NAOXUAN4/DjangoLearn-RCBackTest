from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from CardDetails.models import CardDetailsModel
from .serializer import CardDetailsSerializer


@api_view(['GET'])
def CardDetails(request):
    if request.method == 'GET':
        # 对Course模型进行序列化,many=True表示序列化多个
        s = CardDetailsSerializer(instance=CardDetailsModel.objects.all(), many=True)
        # 返回响应序列化后数据.data
        return Response(data=s.data, status=status.HTTP_200_OK)