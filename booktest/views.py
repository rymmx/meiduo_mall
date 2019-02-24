from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import BookInfo
from .serializers import BookInfoModelSerializer


# 利用DRF中的APIview实现获取所有图书接口
# GET /books/


# """
# 利用:GenericAPIView 实现查询所有图书以及查询指定单一图书的两个接口
# """
# class BookListView(APIView):
#
#     def get(self, request):
#         # 1.获取出查询集
#         qs = BookInfo.objects.all()
#         # 2.创建序列化器进行序列化
#         serializer = BookInfoModelSerializer(qs, many=True)
#
#         # 3.响应response
#         return Response(serializer.data)
#
#
# class BookDetailView(GenericAPIView):
#
#     # 1.指定序列化器类
#     serializer_class = BookInfoModelSerializer
#     # 2.指定查询集
#     queryset = BookInfo.objects.all()
#
#     """详情视图"""
#     def get(self, request, pk):
#         # 1. 获取到要查询的模型对象
#         book = self.get_object()
#         # 2. 创建序列化器进行序列化
#         serializer =self.get_serializer(book)
#         # 3. 响应
#         return Response(serializer.data)


"""
利用:GenericAPIView + mixins扩展来实现获取所有图书和单一图书接口
"""
class BookListView(CreateModelMixin, ListModelMixin, GenericAPIView):
    """列表视图"""
    # 1.指定序列化器类
    serializer_class = BookInfoModelSerializer
    # 2.指定查询集
    queryset = BookInfo.objects.all()

    def get(self, request):
        # # 1. 获取查询集
        # qs = self.get_queryset()
        # # 2. 创建序列化器对象进行序列化操作
        # serializer = self.get_serializer(qs, many=True)
        # # 3. 响应
        # return Response(serializer.data)
        return self.list(request)

    def post(self, request):
        return self.create(request)


class BookDetailView(RetrieveModelMixin, GenericAPIView):

    # 1.指定序列化器类
    serializer_class = BookInfoModelSerializer
    # 2.指定查询集
    queryset = BookInfo.objects.all()

    """详情视图"""
    def get(self, request, pk):
        # # 1. 获取到要查询的模型对象
        # book = self.get_object()
        # # 2. 创建序列化器进行序列化
        # serializer = self.get_serializer(book)
        # # 3. 响应
        # return Response(serializer.data)
        return self.retrieve(request)