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
]