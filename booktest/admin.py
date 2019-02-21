from django.contrib import admin

from .models import BookInfo,HeroInfo

# Register your models here.


# 注册模型到站点
admin.site.register(BookInfo)
admin.site.register(HeroInfo)
