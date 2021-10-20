# -*- coding: utf-8 -*-
# date: 2021/10/20
# Project: OA_system
# File Name: urls.py
# Description: 
# Author: Anefuer_kpl
# Email: 374774222@qq.com

from django.urls import path
from testing import views

urlpatterns = [
    path('img/', views.test)
]