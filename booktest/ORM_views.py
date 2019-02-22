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
# 查询阅读量不大于20，或编号小于3的图书，只能使用Q对象实现
BookInfo.objects.filter(~Q(bread__gt=20) | Q(pk__lt=3))

# 查询阅读量大于20且编号小于3的图书,等价于BookInfo.objects.filter(bread__gt=20, pk__lt=3)
BookInfo.objects.filter(Q(bread__gt=20) & Q(pk__lt=3))


# 以下是聚合函数
BookInfo.objects.aggregate(Sum('bread'))

BookInfo.objects.aggregate(Avg('bread'))

BookInfo.objects.all().order_by('bread')  # 升序
BookInfo.objects.all().order_by('-bread')  # 降序序


# 关联查询
hero1 = HeroInfo.objects.get(hname="令狐冲")
hero1.hbook

"""
在定义模型的时候,如果模型俩个有外键关联,一般把外键定义子多的一方
hbook 会隐式生成一个小写_set属性
"""
book1 = BookInfo.objects.get(id=1)
book1.heroinfo_set  # <django.db.models.fields.related_descriptors.create_reverse_many_to_one_manager.<locals>.RelatedManager object at 0x7f1300d96a58>
book1.heroinfo_set.all()
book1.heroinfo_set.get(hname="黄蓉")

"""关联过滤查询"""
# 一查多
HeroInfo.objects.filter(hbook_id=2)  # <QuerySet [<HeroInfo: 乔峰>, <HeroInfo: 段誉>, <HeroInfo: 王语嫣>]>

# 对应的模型类对象.多对应的模型类名小写_set
b = BookInfo.objects.get(id=1)
b.heroinfo_set.all()


# 多查一
BookInfo.objects.filter(heroinfo__hname="孙悟空")  # <QuerySet [<HeroInfo: 乔峰>, <HeroInfo: 段誉>, <HeroInfo: 王语嫣>]>

# 多对应的模型类对象.多对应的模型类中的关系类属性名
h = HeroInfo.objects.get(id=23)
h.hbook


# 修改
hero = HeroInfo.objects.get(hname='猪八戒')
hero.hname = '猪悟能'
hero.save()

# 使用模型类.objects.filter().update()，会返回受影响的行数
HeroInfo.objects.filter(hname='沙僧').update(hname='沙僧001')

# 模型类对象delete
hero = HeroInfo.objects.get(id=33)
hero.delete()

HeroInfo.objects.filter(id=34).delete()


# 查询集 QuerySet
# 两大特性
# 1.惰性执行  创建查询集不会访问数据库，直到调用数据时，才会访问数据库，调用数据的情况包括迭代、序列化、与if合用
qs=HeroInfo.objects.filter(id=22)
qs

# 2.缓存  使用同一个查询集，第一次使用时会发生数据库的查询，然后Django会把结果缓存下来，再次使用这个查询集时会使用缓存的数据，减少了数据库的查询次数。

# 无缓存,每次都进行数据库查询
from booktest.models import BookInfo
[book.id for book in BookInfo.objects.all()]
[book.id for book in BookInfo.objects.all()]

# 有缓存,不进行数据库查询
qs=BookInfo.objects.all()
[book.id for book in qs]
[book.id for book in qs]
