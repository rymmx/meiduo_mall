from django.conf.urls import url

from . import views


urlpatterns = [
    # 演示提取url路径参数
    # 这里必须分组,和老师演示不一样
    # 演示利用正则组提取url路径参数(位置参数)
    url(r'^weather1/([a-z]+)/(\d{4})/$', views.weather1),

    # 演示利用正则组起别名提取url路径参数(关键字参数)
    url(r'^weather2/(?P<city>[a-z]+)/(?P<year>\d{4})/$', views.weather2),

    # 演示获取请求json数据
    url(r'^get_body_json/$', views.get_body_json),

    # 演示提取请求体表单数据
    url(r'^get_body_form/$', views.get_body_form),

    # 演示提取url问号后面的查询参数
    url(r'^get_query_param/$', views.get_query_param),

    # 演示响应对象使用
    url(r'^response_demo/$', views.response_demo),

    # 演示响应json数据
    url(r'^jsonResponse_demo/$', views.jsonResponse_demo, name='index'),  # name参数是用来给路由起别名

    # 演示反向解析
    url(r'^reverse_demo/$', views.reverse_demo),

]