from django.shortcuts import render
from .models import BookInfo,HeroInfo
# Create your views here.

# 第一种写法
book = BookInfo()
book.btitle = "三国"
book.bpub_date = "1995-11-11"
book.save()

# 第二种写法
book2 = BookInfo(
    btitle="小三国",
    bpub_date="1995-11-11"
)
book2.save()

# 第三种写法
book3 = BookInfo.objects.create(
    btitle="西游记",
    bpub_date="1998-11-11"
)


hero = HeroInfo(
    hname="孙悟空",
    # hbook=book3,  # 外键的关联赋值,和下一句等价
    hbook_id=book3.id,
)


"""以下是基本查询"""
# get/ count /all

BookInfo.objects.get(id=1)
BookInfo.objects.get(id=10)
BookInfo.objects.get(btitle='天龙八部')

BookInfo.objects.all()
BookInfo.objects.count()

