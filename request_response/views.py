import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, reverse, redirect


# Create your views here.


# GET  /weather1/beijing/2018
def weather1(request, city, year):

    print(city)
    print(year)
    return HttpResponse('weather1')


# GET  /weather2/beijing/2018
def weather2(request, year, city):
    # print(request.user)  # AnonymousUser 匿名用户
    print(city)
    print(year)
    return HttpResponse('weather2')


# 演示获取请求体中非表单数据
def get_body_json(request):
    json_str_bytes = request.body
    json_str = json_str_bytes.decode()
    dict1 = json.loads(json_str)
    return HttpResponse('get_body_json')


# 演示获取请求体中的表单数据
# request.POST 属性用来获取请求体中的表单数据 也是得到一个QueryDict类型的对象
def get_body_form(request):
    print(request.body)
    print(request.GET)  # <QueryDict: {'asd': ['456']}>
    print(request.POST)  # <QueryDict: {'a': ['123'], 'like': ['520', '789'], 'abc': ['9999']}>
    a = request.POST.get('a')
    like = request.POST.getlist('like')
    return HttpResponse('get_body_form')


# 演示获取查询参数 ?a=10&b=20&a=30
# request.GET  它是一个属性用来获取查询参数 得到QueryDict
# QueryDict 类型对象 get()方法可以获取一键一值  getlist()方法获取一键多值
def get_query_param(request):
    _=request.GET
    a = request.GET.get('a')
    b = request.GET.get('b')
    alist = request.GET.getlist('a')
    # 变量无类型,对象有类型
    return HttpResponse('get_query_param')


# GET /response_demo/
def response_demo(request):
    """演示响应对象基本使用"""
    # HttpResponse(content=响应体, content_type=响应体数据类型, status=状态码)
    # return HttpResponse(content='hello', content_type='text/html', status=200)
    # return HttpResponse(content='hello', content_type='text/html', status=201)
    return HttpResponse(content='hello', content_type='text/plain', status=201)


# GET  /jsonResponse_demo/
def jsonResponse_demo(request):
    x=request.GET
    # JSON字典中的key必须是字符串并且必须用双引号
    # json_data = {
    #     "name": "cg",
    #     "age": 18
    # }
    json_list_data = [1, 2, 3]  # json数据更喜欢顶层括号是 {}
    # return JsonResponse(json_list_data, safe=False)
    return JsonResponse({'list': json_list_data})


def reverse_demo(request):

    # 如果没有设置路由的命名空间 在reverse中可以(通过视图函数/路由别名)
    # 但是如果写的命名空间,在reverse只能写(命名空间:路由别名)
    print(reverse('request_response:index'))  # 通过函数名去查找它对应路由
    # return HttpResponse('reverse_demo')
    # http://127.0.0.1:8000/reverse_demo/users/index/

    # http://127.0.0.1:8000/users/index/
    # return redirect('/users/index/')
    return redirect(reverse('users:index'))