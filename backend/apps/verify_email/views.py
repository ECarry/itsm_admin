from rest_framework.views import APIView, Response
from rest_framework import status
from random import randint
from django_redis import get_redis_connection
from django.core.mail import send_mail
import re


class VerifyEmail(APIView):
    def get(self, request, email):
        # 验证输入邮箱格式
        match = re.match(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$', email)

        if not match:
            data = {
                'message': '请输入正确邮箱',
                'status': status.HTTP_400_BAD_REQUEST
            }
            return Response(data)

        # 创建6位验证码
        code = '%06d' % randint(0, 999999)

        # 创建 redis 链接
        conn = get_redis_connection('verify_email')

        # 创建 redis 管道
        pl = conn.pipeline()

        # 判断验证码是否 60s 内发送过
        if conn.get('send_flag_%s' % email):
            data = {
                'message': '验证码发送频繁',
                'status': status.HTTP_400_BAD_REQUEST
            }
            return Response(data)

        # 将 邮箱信息及验证码信息存储到 redis。 key timeout value
        pl.setex('email_%s' % email, 300, code)
        pl.setex('send_flag_%s' % email, 60, '1')
        pl.execute()

        # 发送验证码到邮箱
        send_mail(
            subject='【ITSM-admin】注册验证码',
            message='【验证码】： %s ，有效期为5分钟。' % code,
            from_email='569951119@qq.com',
            recipient_list=[email]
        )

        return Response({'message': '发送成功',
                         'status': status.HTTP_200_OK
                         })
