from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet

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


# """
# 利用:GenericAPIView + mixins扩展来实现获取所有图书和单一图书接口
# """
# class BookListView(CreateModelMixin, ListModelMixin, GenericAPIView):
#     """列表视图"""
#     # 1.指定序列化器类
#     serializer_class = BookInfoModelSerializer
#     # 2.指定查询集
#     queryset = BookInfo.objects.all()
#
#     def get(self, request):
#         # # 1. 获取查询集
#         # qs = self.get_queryset()
#         # # 2. 创建序列化器对象进行序列化操作
#         # serializer = self.get_serializer(qs, many=True)
#         # # 3. 响应
#         # return Response(serializer.data)
#         return self.list(request)
#
#     def post(self, request):
#         return self.create(request)
#
#
# class BookDetailView(RetrieveModelMixin, GenericAPIView):
#
#     # 1.指定序列化器类
#     serializer_class = BookInfoModelSerializer
#     # 2.指定查询集
#     queryset = BookInfo.objects.all()
#
#     """详情视图"""
#     def get(self, request, pk):
#         # # 1. 获取到要查询的模型对象
#         # book = self.get_object()
#         # # 2. 创建序列化器进行序列化
#         # serializer = self.get_serializer(book)
#         # # 3. 响应
#         # return Response(serializer.data)
#         return self.retrieve(request)



"""
利用:GenericAPIView + mixins 的合成来形成标准接口
"""
# class BookListView(ListCreateAPIView):
#     """列表视图"""
#     # 1.指定序列化器类
#     serializer_class = BookInfoModelSerializer
#     # 2.指定查询集
#     queryset = BookInfo.objects.all()
#
#
# class BookDetailView(RetrieveAPIView):
#     """详情视图"""
#     # 1.指定序列化器类
#     serializer_class = BookInfoModelSerializer
#     # 2.指定查询集
#     queryset = BookInfo.objects.all()


"""
利用: ViewSet视图集实现查询单一和所有数据接口
"""
# class BookViewSet(ViewSet):
#
#     def list(self, request):
#         qs = BookInfo.objects.all()
#         serializer = BookInfoModelSerializer(qs, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk):
#         try:
#             book = BookInfo.objects.get(id=pk)
#         except BookInfo.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#         serializer = BookInfoModelSerializer(book)
#         return Response(serializer.data)
#


"""
利用: ModelViewSet视图集实现查询单一和所有数据接口
"""
class BookViewSet(ModelViewSet):
    # 指定序列化器
    serializer_class = BookInfoModelSerializer
    # 指定查询集
    queryset = BookInfo.objects.all()

    # /books/latest/
    @action(methods=['get'], detail=False)
    def latest(self, request):
        """获取最后一本图书"""
        book = BookInfo.objects.latest('id')
        serializer = self.get_serializer(book)
        return Response(serializer.data)

    # /books/pk/update_read/
    @action(methods=['put'], detail=True)
    def update_read(self, request, pk):
        """修改图书的阅读量"""
        book = self.get_object()
        book.bread = request.data.get('bread')
        book.save()
        serializer = self.get_serializer(book)
        return Response(serializer.data)
