from django.db import models
import datetime


# Create your models here.

class Manager(models.Model):
    name = models.CharField(max_length=30, verbose_name='管理员名称')
    password = models.CharField(max_length=20, verbose_name='管理员密码')
    '''
    这个参数的默认值也为False，设置为True时，会在model对象第一次被创建时，将字段的值设置为创建时的时间，以后修改对象时，字段的值不会再更新。
    '''
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s' % self.name


class User(models.Model):
    name = models.CharField(max_length=30, verbose_name='用户名称')
    password = models.CharField(max_length=20, verbose_name='用户密码')
    sex = models.CharField(max_length=1, verbose_name='用户性别')

    create_time = models.DateTimeField(auto_now_add=True)
    is_delete = models.CharField(max_length=1, default=0)  # 逻辑删除，默认为0；为1时表示删除

    partment = models.ForeignKey('Partment', on_delete=models.CASCADE, verbose_name='部门外键')  # 和部门表关联
    role = models.ForeignKey('Role', on_delete=models.CASCADE, verbose_name='角色外键')  # 和角色表关联

    create_time = models.DateTimeField(auto_now_add=True)
    is_delete = models.CharField(max_length=1, default=0)  # 逻辑删除，默认为0；为1时表示删除

    def __str__(self):
        return '%s' % self.name


class Role(models.Model):
    num = models.CharField(max_length=10, verbose_name='角色编号')
    name = models.CharField(max_length=30, verbose_name='角色名称')

    create_time = models.DateTimeField(auto_now_add=True)
    is_delete = models.CharField(max_length=1, default=0)  # 逻辑删除，默认为0；为1时表示删除

    def __str__(self):
        return '%s' % self.name


class Company(models.Model):
    name = models.CharField(max_length=30, verbose_name='公司名称')
    phone = models.CharField(max_length=11, verbose_name='公司电话')
    fax = models.CharField(max_length=7, verbose_name='公司传真')
    zipcode = models.CharField(max_length=6, verbose_name='公司邮编')
    site = models.TextField(verbose_name='公司网址')
    bankdeposit = models.CharField(max_length=20, verbose_name='开户行')
    banknum = models.CharField(max_length=30, verbose_name='开户行号')

    create_time = models.DateTimeField(auto_now_add=True)
    is_delete = models.CharField(max_length=1, default=0)  # 逻辑删除，默认为0；为1时表示删除

    def __str__(self):
        return '%s' % self.name


class Partment(models.Model):
    name = models.CharField(max_length=30, verbose_name='部门名称')
    phone = models.CharField(max_length=11, verbose_name='部门电话')
    fax = models.CharField(max_length=7, verbose_name='部门传真')
    function = models.TextField(verbose_name='部门职能')
    num = models.CharField(max_length=10, verbose_name='部门编号')

    prepartment = models.ForeignKey('Partment', on_delete=models.CASCADE, verbose_name='上级部门外键')
    company = models.ForeignKey('Company', on_delete=models.CASCADE, verbose_name='公司外键')

    create_time = models.DateTimeField(auto_now_add=True)
    is_delete = models.CharField(max_length=1, default=0)  # 逻辑删除，默认为0；为1时表示删除

    def __str__(self):
        return '%s' % self.name
