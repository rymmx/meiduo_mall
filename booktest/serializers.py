from rest_framework import serializers

from booktest.models import BookInfo


class BookInfoModelSerializer(serializers.ModelSerializer):
    """定义序列化器"""


    class Meta:
        model = BookInfo
        fields = '__all__'


# class HeroInfoSerializer(serializers.Serializer):
#     """英雄数据序列化器"""
#     GENDER_CHOICES = (
#         (0, 'male'),
#         (1, 'female')
#     )
#     id = serializers.IntegerField(label='ID', read_only=True)
#     hname = serializers.CharField(label='名字', max_length=20)
#     hgender = serializers.ChoiceField(choices=GENDER_CHOICES, label='性别', required=False)
#     hcomment = serializers.CharField(label='描述信息', max_length=200, required=False, allow_null=True)
#     # hbook = serializers.PrimaryKeyRelatedField(label="图书", read_only=True)
#     # hbook = serializers.PrimaryKeyRelatedField(label="图书", queryset=BookInfo.objects.all())
#     # hbook = serializers.StringRelatedField(label="图书", read_only=True)
#     # hbook = BookInfoSerializer(read_only=True)   # 能查出模型所有数据
#
# #
# class BookInfoSerializer(serializers.Serializer):
#     """图书数据序列化器"""
#
#     id = serializers.IntegerField(label='ID', read_only=True)
#     btitle = serializers.CharField(label='名称', max_length=20)
#     bpub_date = serializers.DateField(label='发布日期', required=False)
#     bread = serializers.IntegerField(label='阅读量', required=False)
#     bcomment = serializers.IntegerField(label='评论量', required=False)
#     image = serializers.ImageField(label='图片', required=False)
#
#
#     def validate_btitle(self, value):
#         """对单个字段追加校验逻辑"""
#         if 'django' not in value.lower():
#             raise serializers.ValidationError("图书不是关于Django的")
#
#         return value
#
#     def validate(self, attrs):
#         """同时对多个字段进行追加校验逻辑"""
#         bread = attrs['bread']
#         bcomment = attrs['bcomment']
#         if bread < bcomment:
#             raise serializers.ValidationError('阅读量小于评论量')
#
#         return attrs
#
#
#
#     def create(self, validated_data):
#         """
#         如果创建序列化器时,也会给instant参数传入实参,在调用序列化器的时候
#         :param validated_data:
#         :return:
#         """
#
#         return BookInfo.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """
#         更新,instance为更新的
#         :param instance:
#         :param validated_data:
#         :return:
#         """
#         instance.btitle = validated_data.get('btitle', instance.btitle)
#         instance.bpub_date = validated_data.get('bpub_date', instance.bpub_date)
#         instance.sava()
#         return instance
#
#
# """
# ModelSerializer 模型序列化器
# 想要使用这个类作为序列化器的父类条件:
# 必须有对应的模型,应为他里面不需要定义序列化器字段,他可以根据模型字段自动生成相应的序列化器
# 他里面帮我们实现了create 和 update 方法
# """
#
#
# class BookInfoModelSerializer(serializers.ModelSerializer):
#     """定义序列化器"""
#
#
#     class Meta:
#         model = BookInfo
#         # fields = '__all__'
#         exclude = ['image']  # 除了指定的字段不映射,其他全部映射
#         #
#         extra_kwargs = {
#             'bread': {'min_value': 0},
#             'bcomment': {'min_value': 0},
#             'is_delete': {'write_only': True}
#         }
#         read_only_fields = ['bread', 'bcomment']  #