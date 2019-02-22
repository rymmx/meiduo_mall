from rest_framework import serializers

from booktest.models import BookInfo


class BookInfoSerializer(serializers.ModelSerializer):
    """定义序列化器"""


    class Meta:
        model = BookInfo
        fields = '__all__'