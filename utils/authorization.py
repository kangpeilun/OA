# -*- coding: utf-8 -*-
# date: 2021/10/22
# Project: OA_system
# File Name: authorization.py
# Description: 判断用户是否有权限访问该路由
# Author: Anefuer_kpl
# Email: 374774222@qq.com

from system_manage.models import Manager

# 用户访问该路由时需要处于登陆状态
need_login_path = [
    '/system_manage/manage_center/',
    '/system_manage/user_manage/',
    '/system_manage/role_manage/',
    '/system_manage/company_manage/',
    '/system_manage/partment_manage/',

    '/customer_manage/customer_manage/',
    '/customer_manage/product_manage/',
]

def is_authorized(request):
    path = request.path_info
    print(path, path in need_login_path)
    if path in need_login_path:
        # 如果session中有用户信息，那么可以访问
        if 'uid' in request.session:
            print('具有访问权限')
            uid = request.session['uid']
            manager = Manager.objects.get(id=uid)
            return manager, True
        else:
            return None, False