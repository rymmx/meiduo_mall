import json

from django.http import HttpResponse
from django.shortcuts import render

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