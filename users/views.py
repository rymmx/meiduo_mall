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


#########################################################
# 第二天的
#########################################################


def cookie_demo(request):
    """演示cookie缓存数据的读写"""

    # 创建response对象
    response = HttpResponse('cookie_demo')

    # 写入缓存数据到浏览器的cookie
    response.set_cookie('name', 'rymmx', max_age=3600)

    # 读取cookie
    name = request.COOKIES.get('name')
    print(name)

    return response


def session_demo(request):
    """演示操作session缓存数据的读写"""

    # 将缓存数据写入到session
    request.session["name"] = "rymmx"
    # 上面的代码会将缓存数据存储到redis
    # 在返回响应时生成一个sessionid写入到cookie,将seesionid存储在浏览器中

    # 读取seesion中的缓存数据
    print(request.session.get("name"))
    # 会先从request.COOKIES中读取原先写入的sessionid
    # 在使用sessionid读取redis中存储的那条缓存记录
    # 最后使用指定的key,get出存储的session值

    return HttpResponse("session_demo")