from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=32, verbose_name="姓名")
    mobile = models.CharField(max_length=11, verbose_name="电话")
