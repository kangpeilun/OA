# -*- coding: utf-8 -*-
# date: 2021/10/22
# Project: OA_system
# File Name: paginator.py
# Description: 分页器
# Author: Anefuer_kpl
# Email: 374774222@qq.com

from django.core.paginator import Paginator, Page

def get_pagination_data(paginator, page_obj, around_count=2):
    """
    封装分页器页数相关属性
    :param paginator: 分页器
    :param page_obj: 页面
    :param around_count: 距离...展示的页数
    :return:
    """
    current_page = page_obj.number
    num_pages = paginator.num_pages

    left_has_more = False
    right_has_more = False

    if current_page <= around_count + 2:
        left_pages = range(1, current_page)
    else:
        left_has_more = True
        left_pages = range(current_page - around_count, current_page)

    if current_page >= num_pages - around_count - 1:
        right_pages = range(current_page + 1, num_pages + 1)
    else:
        right_has_more = True
        right_pages = range(current_page + 1, current_page + around_count + 1)
    return {
        'left_pages': left_pages,
        'right_pages': right_pages,
        'current_page': current_page,
        'left_has_more': left_has_more,
        'right_has_more': right_has_more,
        'num_pages': num_pages,
        'num_all': paginator.count,
        'get_split': '?'
    }


def get_pagination_info(queryset, per_page, page_num):
    """
    :param queryset: 查询结果
    :param per_page: 每一个几条数据
    :param page_num: 选取的页面标号
    :return: 所选页，相关数据字典
    """
    paginator = Paginator(queryset, per_page)
    page_data = Paginator.page(paginator, page_num)
    context_data = get_pagination_data(paginator, page_data)
    context = context_data
    context.update({
        'has_previous': page_data.has_previous(),
        'has_next': page_data.has_next(),
        'page_data': page_data
    })
    return page_data.object_list, context