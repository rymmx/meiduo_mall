
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
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

    # 指定过滤字段
    filter_fields = ('id', 'btitle', 'bread')

    # 查询方式: http://127.0.0.1:8000/books/?ordering=-id
    filter_backends = [OrderingFilter]  # 指定过滤后端
    # ordering_fields = ['id', 'bread']  # 指定排序字段
    ordering_fields = ('id', 'bread', 'bpub_date')

    """
    AllowAny 允许所有用户
    IsAuthenticated 仅通过认证的用户
    IsAdminUser 仅管理员用户
    IsAuthenticatedOrReadOnly 认证的用户可以完全操作，否则只能get读取
    """

    # IsAuthenticated 表示只有通过认证(登录用户)的用户才能访问此类视图中的所有接口
    permission_classes = [IsAuthenticatedOrReadOnly]  # The request is authenticated as a user, or is a read-only request.
    # permission_classes = [IsAdminUser]  # Allows access only to admin users.
    # permission_classes = [IsAuthenticated]  # Allows access only to authenticated users.



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


# class BookListView(APIView):
#
#     def get(self, request):
#         qs = BookInfo.objects.all()
#         serializer = BookInfoModelSerializer(qs, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         data = request.data
#         serializer = BookInfoModelSerializer(data=data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)


# class BookDetailView(APIView):
#
#     def put(self, request, pk):
#
#         try:
#             book = BookInfo.objects.get(id=pk)
#         except BookInfo.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         data =request.data
#         serializer = BookInfoModelSerializer(instance=book, data=data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#
#     def delete(self, request, pk):
#         pass

