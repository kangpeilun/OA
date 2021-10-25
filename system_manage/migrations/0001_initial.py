# Generated by Django 2.2.5 on 2021-10-22 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='公司名称')),
                ('phone', models.CharField(max_length=11, verbose_name='公司电话')),
                ('fax', models.CharField(max_length=7, verbose_name='公司传真')),
                ('zipcode', models.CharField(max_length=6, verbose_name='公司邮编')),
                ('site', models.CharField(max_length=100, verbose_name='公司网址')),
                ('bankdeposit', models.CharField(max_length=20, verbose_name='开户行')),
                ('banknum', models.CharField(max_length=30, verbose_name='开户行号')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('is_delete', models.CharField(default=0, max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='管理员名称')),
                ('password', models.CharField(max_length=20, verbose_name='管理员密码')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Partment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='部门名称')),
                ('phone', models.CharField(max_length=11, verbose_name='部门电话')),
                ('fax', models.CharField(max_length=7, verbose_name='部门传真')),
                ('function', models.TextField(verbose_name='部门职能')),
                ('num', models.CharField(max_length=10, verbose_name='部门编号')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('is_delete', models.CharField(default=0, max_length=1)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system_manage.Company', verbose_name='公司外键')),
                ('prepartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system_manage.Partment', verbose_name='上级部门外键')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.CharField(max_length=10, verbose_name='角色编号')),
                ('name', models.CharField(max_length=30, verbose_name='角色名称')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('is_delete', models.CharField(default=0, max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='用户名称')),
                ('password', models.CharField(max_length=20, verbose_name='用户密码')),
                ('sex', models.CharField(max_length=1, verbose_name='用户性别')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('is_delete', models.CharField(default=0, max_length=1)),
                ('partment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system_manage.Partment', verbose_name='部门外键')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system_manage.Role', verbose_name='角色外键')),
            ],
        ),
    ]
