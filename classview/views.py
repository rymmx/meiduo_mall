from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


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