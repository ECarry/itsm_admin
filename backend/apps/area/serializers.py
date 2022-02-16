from rest_framework import serializers
from .models import Area


# 查询所有省，使用 AreaSerializers
# 查询某省的所有市，使用 AreaDetailSerializers 代表某个省，AreaSerializers 为省下的所有市
# 查询某市的所有区县，使用 AreaDetailSerializers 代表某个市，AreaSerializers 为市下的所有区县
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
