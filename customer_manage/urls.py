# -*- coding: utf-8 -*-
# date: 2021/10/22
# Project: OA_system
# File Name: urls.py
# Description: 
# Author: Anefuer_kpl
# Email: 374774222@qq.com

from django.urls import path
from customer_manage import views

urlpatterns = [
    path('customer_manage/', views.customer_manage, name='customer_manage'),
    path('product_manage/', views.product_manage, name='product_manage'),
]