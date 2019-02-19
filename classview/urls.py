from django.conf.urls import url
from . import views

urlpatterns = [

    # url(路由正则,视图函数名称)
    # as_view 将方法变成函数  dispatch 根据请求方法动态查找类视图中的方法
    # 如果把装饰器直接写在定义路由的地方,会把类视图中所有的请求都装饰
    url(r'^demoview/$', views.DemoView.as_view()),

    # 自定义装饰器测试路由
    url(r'^view_func/$', views.view_func),

    # django自带装饰器测试
    url(r'^TestView/$', views.TestView.as_view()),

]
