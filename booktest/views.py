from django.db.models import F, Q, Sum, Avg
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


"""以下是过滤查询"""
BookInfo.objects.filter(btitle__contains="天")
# BookInfo.objects.filter(id__exact=1)
BookInfo.objects.filter(id=1)

BookInfo.objects.filter(btitle__endswith="部")

BookInfo.objects.filter(btitle__isnull=False)

BookInfo.objects.filter(id__in=[2,4])  # id__in不是指定范围,而是指定具体几个

BookInfo.objects.filter(id__gt=2)

BookInfo.objects.filter(id__lt=2)

# 查询除id>=2以外的书
BookInfo.objects.filter(id__gte=2)

# 查询除id=3以外的书
BookInfo.objects.exclude(id=3)

# 查询1980年发布的书
BookInfo.objects.filter(bpub_date__year=1980)

# 查询1990-1-1发布的书籍
BookInfo.objects.filter(bpub_date__gt="1990-1-1")


# F对象,对两个字段进行比较
# 查询阅读量大于评论量的书籍
BookInfo.objects.filter(bread__gt=F('bcomment'))

# 查询阅读量大于评论量2倍的书籍
BookInfo.objects.filter(bread__gt=F('bcomment')*2)


# Q对象   多个过滤器逐个调用表示逻辑与关系，同sql语句中where部分的and关键字
# id<=3,并且bread 要大于30
BookInfo.objects.filter(id__lte=3,bread__gt=30)

# Q对象可以使用&、|连接，&表示逻辑与，|表示逻辑或。
# 查询阅读量大于20，或编号小于3的图书，只能使用Q对象实现
BookInfo.objects.filter(Q(bread__gt=20) | Q(pk__lt=3))

# 查询阅读量大于20且编号小于3的图书,等价于BookInfo.objects.filter(bread__gt=20, pk__lt=3)
BookInfo.objects.filter(Q(bread__gt=20) & Q(pk__lt=3))


# 以下是聚合函数
BookInfo.objects.aggregate(Sum('bread'))

BookInfo.objects.aggregate(Avg('bread'))

BookInfo.objects.all().order_by('bread')  # 升序
BookInfo.objects.all().order_by('-bread')  # 降序序


# 关联查询
