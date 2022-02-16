from rest_framework import serializers
from .models import Area


class AreaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ['id', 'name']


class AreaDetailSerializers(serializers.ModelSerializer):
    subs = AreaSerializers(many=True)
    # subs = serializers.PrimaryKeyRelatedField()   # 只会序列化出 id
    # subs = serializers.StringRelatedField()       # 序列化是模型中 str 返回的值

    class Meta:
        model = Area
        fields = ['id', 'name', 'subs']
