from django.contrib import admin
from django.contrib.admin import TabularInline,StackedInline

from .models import BookInfo,HeroInfo

# Register your models here.
# 想要自定义admin站点管理界面需要定义模型站点管理类


class HeroInfoInline(StackedInline):  # 以块展示
# class HeroInfoInline(TabularInline):  # 以表展示
    model = HeroInfo  #指定关联展示哪个模型数据
    extra = 1  # 额外的编辑框
    pass


class BookInfoAdmin(admin.ModelAdmin):
    """书籍模型管理类"""

    """以下代码是调整编辑界面"""
    # 设置每页显示数据条数
    list_per_page = 4

    # 设置操作选项
    actions_on_top = False
    actions_on_bottom = True
    # 列表界面显示那些字段/列
    # list_display = ('模型属性', '模型中的方法名')/[]  '1991-11-11'
    list_display = ["id", "btitle", "bpub_date", "bread", "bcomment", "pub_date_format"]

    """以下代码是调整编辑页面"""
    # fields = ["btitle", 'bpub_date', 'is_delete']  # 编辑页面可以进行编辑字段默认模型中的字段可以编辑

    fieldsets = [
        ["基础组", {'fields': ['btitle', "bpub_date","image"]}],
        ["高级组", {'fields': ["bread",'bcomment','is_delete'],
                 'classes': ['collapse']  # 设置CSS可折叠属性
                 },]
    ]

    # 下面这个属性只能用在一对多模型一的那方
    inlines = [HeroInfoInline]  # 编辑页面关联展示的页面


@admin.register(HeroInfo)  # 第二种写法
class HeroInfoAdmin(admin.ModelAdmin):
    """英雄模型管理类"""

    list_per_page = 5
    list_display = ["id", "hname", "hbook", "hgender", "hcomment", "read"]

    # 右侧过滤栏
    list_filter = ["hbook", "hgender"]
    # 顶部搜索框
    search_fields = ["id", "hname"]


# 注册模型到站点
admin.site.register(BookInfo, BookInfoAdmin) # 第一种写法
# admin.site.register(HeroInfo, HeroInfoAdmin)


# 以下三行代码对于整个站点只用配置一次
admin.site.site_header = '我的书城'
admin.site.site_title = '我的书城MIS'
admin.site.index_title = '欢迎使用我的书城MIS'