from django.conf.urls import url
from . import views

urlpatterns = [

    # url(路由正则,视图函数名称)
    # as_view 将方法变成函数  dispatch 根据请求方法动态查找类视图中的方法
    url(r'^demoview/$', views.DemoView.as_view()),

]
