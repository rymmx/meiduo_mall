from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from booktest import views

urlpatterns = [
    # url(r'^books/$', views.BookListView.as_view()),
    # url(r'^books/(?P<pk>\d+)/$', views.BookDetailView.as_view()),
    # url(r'^books/$',views.BookViewSet.as_view({'get':'list', 'post':'create'})),
    # url(r'^books/(?P<pk>\d+)/$', views.BookViewSet.as_view({'get': 'retrieve'})),

    # url(r'^books/latest/$', views.BookViewSet.as_view({'get': 'latest'})),
    # url(r'^books/(?P<pk>\d+)/update_read/$', views.BookViewSet.as_view({'put': 'update_read'})),

]


# # 创建路由器
# base_name 如果base_name参数不传递它内部会使用queryset中指定的查询集 模型名作为base_name路由别名前缀,如果没有给queryset类属性指定查询集,就必须要给base_name参数传参不然就会报错
router = DefaultRouter()
# # 将视图注册到路由
router.register(r'books', views.BookViewSet)  # 注册路由指定路由前缀和指定视图集
# # 视图集路由添加到urlpatterns
urlpatterns += router.urls  # 把路由器生成好的路由追加到路由列表中
# # urlpatterns = urlpatterns + router.urls


print(router.urls)

"""
[<RegexURLPattern bookinfo-list ^books/$>, 
<RegexURLPattern bookinfo-list ^books\.(?P<format>[a-z0-9]+)/?$>, 
<RegexURLPattern bookinfo-detail ^books/(?P<pk>[^/.]+)/$>, 
<RegexURLPattern bookinfo-detail ^books/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$>, 
<RegexURLPattern api-root ^$>, 
<RegexURLPattern api-root ^\.(?P<format>[a-z0-9]+)/?$>]
"""

"""
[<RegexURLPattern bookinfo-list ^books/$>, 
<RegexURLPattern bookinfo-list ^books\.(?P<format>[a-z0-9]+)/?$>, 
<RegexURLPattern bookinfo-latest ^books/latest/$>, 
<RegexURLPattern bookinfo-latest ^books/latest\.(?P<format>[a-z0-9]+)/?$>, 
<RegexURLPattern bookinfo-detail ^books/(?P<pk>[^/.]+)/$>, 
<RegexURLPattern bookinfo-detail ^books/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$>, 
<RegexURLPattern bookinfo-update-read ^books/(?P<pk>[^/.]+)/update_read/$>, 
<RegexURLPattern bookinfo-update-read ^books/(?P<pk>[^/.]+)/update_read\.(?P<format>[a-z0-9]+)/?$>, 
<RegexURLPattern api-root ^$>, 
<RegexURLPattern api-root ^\.(?P<format>[a-z0-9]+)/?$>]

"""