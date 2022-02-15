from rest_framework import serializers
from django_redis import get_redis_connection
from .models import User


class CreateUserSerializers(serializers.ModelSerializer):
    # 所有字段 ['id', 'username', 'name', 'email', 'mobile', 'password', 'checkPass', 'code']
    # 已存在字段 ['id', 'username', 'name', 'email', 'mobile', 'password']
    # 需要序列化字段（输出前段）字段 ['id', 'username', 'name', 'email', 'mobile']
    # 反序列化字段 ['username', 'name', 'email', 'mobile', 'password', 'checkPass', 'code']
    checkPass = serializers.CharField(required=True, write_only=True, label="确认密码")
    verifyCode = serializers.CharField(max_length=6, required=True, write_only=True, label="验证码")

    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'checkPass', 'verifyCode']
        # 修改默认字段
        extra_kwargs = {
            'username': {
                'min_length': 5,
                'max_length': 32,
                'error_messages': {
                    'min_length': '用户名字符小于5个',
                    'max_length': '用户名字符大于32个',
                }
            },
            'password': {
                'min_length': 8,
                'max_length': 32,
                'error_messages': {
                    'min_length': '密码字符小于8个',
                    'max_length': '密码字符大于32个',
                }
            },
        }

    def validate(self, attrs):
        # 校验用户输入两次密码是否正确
        if attrs['password'] != attrs['checkPass']:
            raise serializers.ValidationError('两次密码输入不一致')

        # 验证用户输入的验证码
        conn = get_redis_connection('verify_email')
        real_code = conn.get('email_%s' % attrs['email'])
        # 从 redis 取出的数据为 bytes，需要转码
        if real_code is None or real_code.decode() != attrs['verifyCode']:
            raise serializers.ValidationError('验证码错误')

        return attrs

    def create(self, validated_data):
        # 移除不需要的字段
        del validated_data['checkPass']
        del validated_data['verifyCode']

        # 从 validated_data 去除密码并从中删除
        password = validated_data.pop('password')

        user = User(**validated_data)
        # 加密密码
        user.set_password(password)
        user.save()

        return user

