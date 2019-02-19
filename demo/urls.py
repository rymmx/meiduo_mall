"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
# from users import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # 将users子应用的所有路由包含到总路由中
    # url(r'^users/', include('users.urls')),
    # 如果某个功能模块的所有路由 都是以相同前缀开头 那可以把路由的前缀写在总路由

    # 只在总路由里面去定义路由信息
    # url(r'^users/index/$', views.index),

    # 只在总路由中包含子应用的所有路由,将子应用的所有路由信息全部写在子应用中
    # url(r'^', include('users.urls'),
    url(r'^', include('users.urls', namespace='users')),

    # 演示请求和响应子应用的所有路由
    url(r'^', include('request_response.urls', namespace='request_response')),

    # 类视图
    url(r'^', include('classview.urls')),

]
