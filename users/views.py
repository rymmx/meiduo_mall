from django.shortcuts import render,reverse,redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    # x=request
    """
    django标准函数视图  两个要求 必须要有一个参数来接收请求对象,必须在函数的最后响应了一个HttpResponse
    :param request: 接收到请求  HttpRequest/WsgiRequest
    :return: HttpResponse() 响应对象 不能直接返回字符串
    """
    return HttpResponse("hello Django...")


# /users/sayhello
def say_hello(request):
    return HttpResponse('say_hello')


# /users/say
def say(request):
    return HttpResponse('say')


#  http://127.0.0.1:8000/users/index/?a=10&b=20
def indexabc(request):
    """
    django标准函数视图  两个要求 必须要有一个参数来接收请求对象,必须在函数的最后响应了一个HttpResponse
    :param request: 接收到请求  HttpRequest/WsgiRequest
    :return: HttpResponse() 响应对象 不能直接返回字符串
    """
    # 不能有namespace,先反向解析出视图路径,通过路径重定向,reverse等价于flask中的url_for
    # print(reverse(index))
    # print("-------")
    # return redirect(reverse(index))

    # 次方法必须要在总路由中有namespace="users"
    print(reverse('users:index'))
    print("-------")
    return redirect(reverse('users:index'))