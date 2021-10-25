from django.shortcuts import render, HttpResponse, redirect, reverse, render_to_response
from system_manage.models import Manager, User, Role, Company, Partment
from utils.paginator import get_pagination_info
from utils.authorization import is_authorized


# Create your views here.
# ============================== ↓管理员管理 ===================================
def login(request):
    name = request.POST.get('name')
    password = request.POST.get('password')

    manager = Manager.objects.filter(name=name).first()
    if manager:
        if manager.password == password:
            request.session['uid'] = manager.id
            return redirect(reverse('manage_center'))  # 用户名密码正确进入系统主页
        return HttpResponse('用户名或密码错误')
    return render(request, 'login.html')


def register(request):
    name = request.POST.get('name')
    password = request.POST.get('password')

    manager = Manager()
    manager.name = name.strip()
    manager.password = password.strip()
    manager.save()

    return redirect(reverse('login'))


def manage_center(request):
    manager, authoried = is_authorized(request)
    # 如果没有被授权，则将重定向到登陆页面
    if not authoried:
        return redirect(reverse('login'))

    # 如果被授权，则进入管理中心
    name = manager.name
    context = {
        'name': name,
    }
    return render(request, 'manage_center.html', context=context)


# ============================== ↑管理员管理 ===================================

# ============================== 用户信息管理 ===================================
def user_manage(request):
    manager, authoried = is_authorized(request)
    # 如果没有被授权，则将重定向到登陆页面
    if not authoried:
        return redirect(reverse('login'))

    # 如果是post请求，则添加用户信息
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        sex = request.POST.get('sex')
        partment = request.POST.get('partment')
        role = request.POST.get('role')

        user = User()
        user.name = name.strip()
        user.password = password.strip()
        user.sex = sex.strip()
        partment = Partment.objects.get(name=partment.strip())
        role = Role.objects.get(name=role.strip())
        if partment:
            # 如果在Partment表中查到对应部门 建立外键关系
            user.partment = partment

        if role:
            # 如果在Role表中查到对应角色 建立外键关系
            user.role = role

        user.save()

        return redirect(reverse('user_manage'))

    # 如果不是POST请求，则正常显示查询到的结果
    users = User.objects.all()
    pagesize = 10  # 每页显示的数据条数
    pagenum = int(request.GET.get('p', 1))  # 要显示的页码, 默认显示第一页
    page, context = get_pagination_info(users, pagesize, pagenum)  # 分页处理
    context.update({
        'the_url': reverse('user_manage'),
        'page': page
    })

    return render(request, 'system_manage/userManage.html', context=context)


# ============================== 角色信息管理 ===================================
def role_manage(request):
    manager, authoried = is_authorized(request)
    # 如果没有被授权，则将重定向到登陆页面
    if not authoried:
        return redirect(reverse('login'))

    # 如果是post请求，则添加用户信息
    if request.method == 'POST':
        num = request.POST.get('num')
        name = request.POST.get('name')

        role = Role()
        role.num = num.strip()
        role.name = name.strip()
        role.save()

        return redirect(reverse('role_manage'))

    # 如果不是POST请求，则正常显示查询到的结果
    roles = Role.objects.all()
    pagesize = 10  # 每页显示的数据条数
    pagenum = int(request.GET.get('p', 1))  # 要显示的页码
    page, context = get_pagination_info(roles, pagesize, pagenum)  # 分页处理
    context.update({
        'the_url': reverse('role_manage'),
        'page': page
    })

    return render(request, 'system_manage/roleManage.html', context=context)


# ============================== 企业信息管理 ===================================
def company_manage(request):
    manager, authoried = is_authorized(request)
    # 如果没有被授权，则将重定向到登陆页面
    if not authoried:
        return redirect(reverse('login'))

    # 如果是post请求，则添加用户信息
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        fax = request.POST.get('fax')
        zipcode = request.POST.get('zipcode')
        site = request.POST.get('site')
        bankdeposit = request.POST.get('bankdeposit')
        banknum = request.POST.get('banknum')

        company = Company()
        company.name = name.strip()
        company.phone = phone.strip()
        company.fax = fax.strip()
        company.zipcode = zipcode.strip()
        company.site = site.strip()
        company.bankdeposit = bankdeposit.strip()
        company.banknum = banknum.strip()

        company.save()

        return redirect(reverse('company_manage'))

    # 如果不是POST请求，则正常显示查询到的结果
    companys = Company.objects.all()
    pagesize = 10  # 每页显示的数据条数
    pagenum = int(request.GET.get('p', 1))  # 要显示的页码
    page, context = get_pagination_info(companys, pagesize, pagenum)  # 分页处理
    context.update({
        'the_url': reverse('user_manage'),
        'page': page
    })

    return render(request, 'system_manage/companyManage.html', context=context)


# ============================== 部门信息管理 ===================================
def partment_manage(request):
    manager, authoried = is_authorized(request)
    # 如果没有被授权，则将重定向到登陆页面
    if not authoried:
        return redirect(reverse('login'))

    # 如果是post请求，则添加用户信息
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        fax = request.POST.get('fax')
        prepartment = request.POST.get('prepartment')
        function = request.POST.get('function')
        num = request.POST.get('num')
        company = request.POST.get('company')

        partment = Partment()
        partment.name = name.strip()
        partment.phone = phone.strip()
        partment.fax = fax.strip()
        partment.function = function.strip()
        partment.num = num.strip()

        company = Company.objects.get(name=company.strip())
        prepartment = Partment.objects.get(name=prepartment.strip())
        if company:
            # 如果在Company表中查到对应公司 建立外键关系
            partment.company = company

        if prepartment:
            # 如果在Partment表中查到对应部门 建立外键关系
            partment.prepartment = prepartment

        partment.save()

        return redirect(reverse('partment_manage'))

    # 如果不是POST请求，则正常显示查询到的结果
    partments = Partment.objects.all()
    pagesize = 10  # 每页显示的数据条数
    pagenum = int(request.GET.get('p', 1))  # 要显示的页码
    page, context = get_pagination_info(partments, pagesize, pagenum)  # 分页处理
    context.update({
        'the_url': reverse('user_manage'),
        'page': page
    })

    return render(request, 'system_manage/partmentManage.html', context=context)


# ============================== 删除信息 ===================================
# TODO: 使用一个视图函数控制所有的表的删除, 可以实现批量删除
def delete_info(request):
    manager, authoried = is_authorized(request)
    # 如果没有被授权，则将重定向到登陆页面
    if not authoried:
        return redirect(reverse('login'))

    pass
