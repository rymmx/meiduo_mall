from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View


# Create your views here.


class DemoView(View):
    """类视图"""

    def get(self,request):
        # x,y,z debug用
        x = self.request
        y = self.args
        z = self.kwargs
        return HttpResponse('get请求业务逻辑')

    def post(self,request):
        return HttpResponse('post请求业务逻辑')


def my_decorator(view_func):
    """
    装饰器
    :param view_func: 被装饰的函数
    :return: wrapper
    """

    def wrapper(request, *args, **kwargs):
        print('my_decorator装饰器被调用了')
        print(request.method, request.path)
        # 调用被装饰的函数视图
        return view_func(request, *args, **kwargs)

    return wrapper


@my_decorator
def view_func(request):
    return HttpResponse('view_func')


# django自带装饰器,解决自定义装饰器传参错乱问题
@method_decorator(my_decorator, name='get')
class TestView(View):
    """类视图的定义和使用"""

    def get(self, request):
        """GET请求业务逻辑"""
        return HttpResponse('get')

    @method_decorator(my_decorator)  # 装饰类中的方法
    def post(self, request):
        """POST请求业务逻辑"""
        return HttpResponse('post')

