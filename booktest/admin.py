from django.contrib import admin

from .models import BookInfo,HeroInfo

# Register your models here.
# 想要自定义admin站点管理界面需要定义模型站点管理类


class BookInfoAdmin(admin.ModelAdmin):
    """书籍模型管理类"""

    """以下代码是调整编辑界面"""
    # 设置每页显示数据条数
    list_per_page = 4

    # 设置操作选项
    actions_on_top = False
    actions_on_bottom = True
    # 列表界面显示那些字段/列
    list_display = ["id", "btitle", "bpub_date", "bread", "bcomment", "pub_date_format"]

    """以下代码是调整编辑页面"""
    # fields = ["btitle", 'bpub_date', 'is_delete']  # 编辑页面可以进行编辑字段默认模型中的字段可以编辑

    fieldsets = [
        ["基础组", {'fields': ['btitle', "bpub_date"]}],
        ["高级组", {'fields': ["bread",'bcomment','is_delete'],
                 'classes': ['collapse']
                 },]
    ]
    pass


@admin.register(HeroInfo)  # 第二种写法
class HeroInfoAdmin(admin.ModelAdmin):
    """书籍模型管理类"""

    list_display = ["id", "hname", "hgender", "hcomment", "hbook", "read"]

    list_filter = ["hbook", "hgender"]

    search_fields = ["hname", "hcomment"]
    pass


# 注册模型到站点
admin.site.register(BookInfo, BookInfoAdmin) # 第一种写法
# admin.site.register(HeroInfo, HeroInfoAdmin)
