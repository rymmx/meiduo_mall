from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from booktest import views

urlpatterns = [
    # url(r'^books/$', views.BookListVIew.as_view()),
    # url(r'^books/(?P<pk>\d+)/$', views.BookDetailView.as_view())
]


# 创建路由器
router = DefaultRouter()
router.register(r'books', views.BookInfoViewSet)
urlpatterns += router.urls
# urlpatterns = urlpatterns + router.urls