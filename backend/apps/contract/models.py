from django.db import models


class Contract(models.Model):
    contract_num = models.CharField(max_length=32, verbose_name="合同编号")
    contract_date = models.DateField(verbose_name="签订日期")
    project_num = models.CharField(max_length=32, verbose_name="项目编号")
    start_date = models.DateField(verbose_name="开工日期")
    area = models.CharField(max_length=32, verbose_name="区域")
    contract_name = models.CharField(max_length=256, verbose_name="合同名称")
    custom = models.CharField(max_length=128, verbose_name="客户名称")
    end_date = models.DateField(verbose_name="结束日期")
    tele_contract_num = models.CharField(max_length=32, blank=True, verbose_name="电信合同编码")
    total_sum = models.FloatField(verbose_name="总金额")

    def __str__(self):
        pass
