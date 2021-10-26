"""OA_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from system_manage import views as sys_views
import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', sys_views.login, name='login'),   # 登录
    path('logout/', sys_views.logout, name='logout'),  # 退出登录
    path('register/', sys_views.register, name='register'),    # 注册
    path('system_manage/', include('system_manage.urls')),  # 系统管理
    path('customer_manage/', include('customer_manage.urls')),   # 客户管理
]

# handler404 = views.page_not_found  # 404页面