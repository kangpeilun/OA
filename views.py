# -*- coding: utf-8 -*-
# date: 2021/10/22
# Project: OA_system
# File Name: views.py
# Description: 
# Author: Anefuer_kpl
# Email: 374774222@qq.com

from django.shortcuts import render

# ============================== 处理404页面 ===================================
def page_not_found(request, exception):
    return render(request, '404.html')