from rest_framework.views import APIView
from rest_framework.response import Response

from .models import BookInfo
from .serializers import BookInfoModelSerializer


# 利用DRF中的APIview实现获取所有图书接口
# GET /books/


class BookListView(APIView):

    def get(self, request):
        # 1.获取出查询集
        qs = BookInfo.objects.all()
        # 2.创建序列化器进行序列化
        serializer = BookInfoModelSerializer(qs, many=True)

        # 3.响应response
        return Response(serializer.data)