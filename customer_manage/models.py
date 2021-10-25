from django.db import models


# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=30, verbose_name='客户名称')
    briefinfo = models.TextField(verbose_name='客户简介')
    area = models.CharField(max_length=30, verbose_name='所属地区')
    type = models.CharField(max_length=20, verbose_name='客户类型')
    nature = models.CharField(max_length=20, verbose_name='企业性质')
    describe = models.TextField(verbose_name='企业描述')

    create_time = models.DateTimeField(auto_now_add=True)
    is_delete = models.CharField(max_length=1, default=0)  # 逻辑删除，默认为0；为1时表示删除

    def __str__(self):
        return '%s' % self.name


class Product(models.Model):
    name = models.CharField(max_length=30, verbose_name='产品名称')
    supplier = models.CharField(max_length=20, verbose_name='供应商')
    num = models.CharField(max_length=10, verbose_name='产品编号')
    type = models.CharField(max_length=20, verbose_name='产品类型')
    price = models.CharField(max_length=10, verbose_name='出售价')
    describe = models.TextField(verbose_name='产品描述')

    create_time = models.DateTimeField(auto_now_add=True)
    is_delete = models.CharField(max_length=1, default=0)  # 逻辑删除，默认为0；为1时表示删除

    def __str__(self):
        return '%s' % self.name
