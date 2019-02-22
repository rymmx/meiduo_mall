import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.


from datetime import datetime

from django.views import View

from booktest.models import BookInfo


class BookListVIew(View):
    """
    查询所有图书、增加图书
    """
    def get(self, request):
        """
        查询所有图书
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

        json_bytes = request.body
        json_str = json_bytes.decode()
        book_dict = json.loads(json_str)

        # 此处需要校验先省略

        book = BookInfo.objects.create(
            btitle=book_dict.get('btitle'),
            bpub_date=book_dict.get('bpub_date')
        )

        json_dict = {
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment,
            'image': book.image.url if book.image else ''
        }

        return JsonResponse(json_dict, status=201)


class BookDetailView(View):
    """查询指定图书, 修改指定图书, 删除指定图书"""

    def get(self, request, pk):
        """GET  /books/<pk>  提供指定id的记录"""
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

