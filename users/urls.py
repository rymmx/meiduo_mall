# 定义子应用的所有路由信息
from django.conf.urls import url

from . import views

urlpatterns = [
    # url(url路径正则, 函数视图名)
    # 演示路由匹配查找视图
    # url(r'^index/$', views.index),
    url(r'^users/index/$', views.index, name='index'),

    # 演示路由匹配顺序: 自上而下一个一个去匹配
    # url(r'^users/say', views.say),
    # url(r'^users/sayhello', views.say_hello),
    # 演示路由匹配顺序: 自上而下一个一个去匹配
    # 定义路由时,一定要有严格的开头和结尾  ^ $
    url(r'^say/$', views.say),
    url(r'^sayhello/$', views.say_hello),

    # 如果定义路由时没有写最后的 斜杠 那么在浏览中多加了 斜杠   404
    # 如果定义路由时最后加了 斜杠 那么在浏览中 最后自己写不写 斜杠都能找到视图,原因是浏览器会自动重定向到加 斜杠

    # 把路由全部写在子应用中
    url(r'^users/indexabc/$', views.indexabc),
]