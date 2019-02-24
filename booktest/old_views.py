import json
from django.http import JsonResponse, HttpResponse
from django.views import View
from rest_framework.viewsets import ModelViewSet
from booktest.serializers import BookInfoModelSerializer
from booktest.models import BookInfo, HeroInfo
from booktest.serializers import BookInfoSerializer,HeroInfoSerializer

# Create your views here.

"""
GET     /books/         提供所有记录
POST    /books/         新增一条记录
GET     /books/<pk>/    提供指定id的记录
PUT     /books/<pk>/    修改指定id的记录
DELETE  /books/<pk>/    删除指定id的记录

响应数据    JSON
"""


class BookListVIew(View):
    """
    查询所有图书、增加图书
    """
    def get(self, request):
        """
        1.查询所有图书模型对象
        2.把模型转换位JSON字典
        3.响应
        路由：GET /books/
        """
        queryset = BookInfo.objects.all()
        book_list = []
        for book in queryset:
            book_list.append({
                'id': book.id,
                'btitle': book.btitle,
                'bpub_date': book.bpub_date,
                'bread': book.bread,
                'bcomment': book.bcomment,
                'image': book.image.url if book.image else ''
            })
        return JsonResponse(book_list, safe=False)

    def post(self, request):
        """POST  /books/  新增一条记录"""
        # 1.获取请求中的JSON数据
        # 2.把bytes类型的数据转换为JSON字典
        # 前端传入的数据不能直接使用,都必须经过校验
        # 3.创建模型对象,赋值并存储到数据库
        # 4.响应

        json_bytes = request.body
        json_str = json_bytes.decode()
        book_dict = json.loads(json_str)

        # 此处需要校验先省略

        #概念:  将其他格式（字典、JSON、XML等）转换为程序中的数据，例例如将JSON字符串串转换为Django中的模型类对象，这个过程我们称为反序列列化
        book = BookInfo.objects.create(
            btitle=book_dict.get('btitle'),
            bpub_date=book_dict.get('bpub_date')
        )

        #  将程序中的⼀一个数据结构类型转换为其他格式（字典、JSON、XML等），例例如将Django中的模型类对象转换为JSON字符串串，这个转换过程我们称为序列列化。
        json_dict = {
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment,
            'image': book.image.url if book.image else ''
        }

        return JsonResponse(json_dict, status=201)
        # 在开发REST API接⼝口时，我们在视图中需要做的最核⼼心的事是：
        # • 将数据库数据序列列化为前端所需要的格式，并返回；
        # • 将前端发送的数据反序列列化为模型类对象，并保存到数据库中。


class BookDetailView(View):
    """查询指定图书, 修改指定图书, 删除指定图书"""

    def get(self, request, pk):
        """GET  /books/<pk>  提供指定id的记录"""
        # 1.查询出pk所指定的那个数据
        # 2.把模型对象转换为字典
        # 3.响应
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse(status=404)

        json_dict = {
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment,
            'image': book.image.url if book.image else ''
        }

        return JsonResponse(json_dict)

    def put(self, request, pk):
        """PUT  /books/<pk>  修改指定id的记录"""
        # 0.获取前段传入的数据(校验)
        # 1.获取要修改的模型对象
        # 2.修改模型属性值
        # 3. save()

        json_bytes = request.body
        json_str = json_bytes.decode()
        book_dict = json.loads(json_str)

        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse(status=404)

        # 此处需要校验先省略

        book.btitle = book_dict.get('btitle')
        book.bpub_date = book_dict.get('bpub_date')
        book.save()

        json_dict = {
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment,
            'image': book.image.url if book.image else ''
        }

        return JsonResponse(json_dict)

    def delete(self, request, pk):
        """DELETE  /books/<pk>  删除指定id的记录"""
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse(status=404)

        book.delete()

        return HttpResponse(status=204)


class BookInfoViewSet(ModelViewSet):
    """定义视图集"""

    # 指定序列化器
    serializer_class = BookInfoModelSerializer
    # 指定查询
    queryset = BookInfo.objects.all()


# book = BookInfo.objects.get(id=1)
# # 创建序列化器进行序列化器
# # 给instance参数传入实参  可以传模型/查询集(many=True)/字典
# serializer = BookInfoSerializer(instance=book)
# # serializer = BookInfoSerializer(book)  # 同上一句
# serializer.data
#
#
# #序列化查询集QuerySet
# book_qs = BookInfo.objects.all()
# serializer = BookInfoSerializer(book_qs, many=True)
# serializer.data
#
# # 上面的另一种写法
# book_qs = BookInfo.objects.all()
# serializer = BookInfoSerializer({"books":book_qs})  # 有BUG,不要这样写
# serializer.books
#
#
# # 关联序列化
# hero = HeroInfo.objects.get(id=1)
# serializer = HeroInfoSerializer(hero)
# serializer.data
#
#
# # 反序列化演练
# from booktest.serializers import BookInfoSerializer
# data = {
#     "btitle": "三国Django",
#     'bpub_date': '1991-11-11',
#     "bread": 20,
#     "bcomment": 19,
# }
# serializer = BookInfoSerializer(data=data)
# serializer.is_valid(raise_exception=True)
# a = serializer.save()  # 将校验后的数据修改到数据库
#     # 当序列化器调用save方法 会去执行序列化器中的create方法或update方法
#     # serializer.data
