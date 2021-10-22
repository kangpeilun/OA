# 环境要求

```python
python=3.7
Django=2.2
```



## 1.数据库创建

```python
# 进入数据库
mysql -uroot -proot

# 创建 oasystem 数据库
create database oasystem charset=utf8;
```

## 项目技巧

### 1.配置404页面

Required: **settings.py 文件中必须修改的两项**

```python
DEBUG = False  # 必须取消debug模式

ALLOWED_HOSTS = ['*']  # 必须配置可以访问的
```

在主程序下新建views.py文件

```python

# 并在该文件中写入

from django.shortcuts import render

# ============================== 处理404页面 ===================================
def page_not_found(request, exception):
    return render(request, '404.html')

def page_permission_denied(request):
    return render(request, '404.html')

def page_inter_error(request):
    return render(request, '404.html')
```

在主路由中配置404页面

```python
from django.contrib import admin
from django.urls import path, include
from system_manage import views as sys_views
import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', sys_views.login, name='login'),   # 登录
    path('register/', sys_views.register, name='register'),    # 注册
    path('system_manage/', include('system_manage.urls')),  # 系统管理
    path('customer_manage/', include('customer_manage.urls')),   # 客户管理
]

handler403 = view.page_permission_denied
handler404 = views.page_not_found  # 404页面
handler500 = view.page_inter_error
```





## 2.遇到的问题及解决办法

### 1.fatal: unable to access 'https://github.com/kangpeilun/OA_system.git/': OpenSSL SSL_read: Connection was reset, errno 10054

```python
在开启shadowsock的前提下，手动配置git的代理。git客户端输入如下两个命令就可以了。

git config --global http.proxy http://127.0.0.1:1080

git config --global https.proxy http://127.0.0.1:1080
```

