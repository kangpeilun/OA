# -*- coding: utf-8 -*-
# date: 2021/10/22
# Project: OA_system
# File Name: urls.py
# Description: 
# Author: Anefuer_kpl
# Email: 374774222@qq.com

from django.urls import path
from system_manage import views

urlpatterns = [
    path('manage_center/', views.manage_center, name='manage_center'),
    path('user_manage/', views.user_manage, name='user_manage'),
    path('role_manage/', views.role_manage, name='role_manage'),
    path('company_manage/', views.company_manage, name='company_manage'),
    path('partment_manage/', views.partment_manage, name='partment_manage'),
]