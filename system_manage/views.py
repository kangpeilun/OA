from django.shortcuts import render, HttpResponse, redirect, reverse, render_to_response
from system_manage.models import Manager, User, Role, Company, Partment
from utils.paginator import get_pagination_info
from utils.authorization import is_authorized


# Create your views here.
# ============================== ↓管理员管理 ===================================
def login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')

        manager = Manager.objects.filter(name=name).first()
        print('manager',manager)
        if manager:
            if manager.password == password:
                request.session['uid'] = manager.id
                return HttpResponse('登陆成功', status=200)  # 用户名密码正确进入系统主页
            return HttpResponse('用户名或密码错误', status=400)
        return HttpResponse('用户名或密码错误', status=400)

    return render(request, 'login.html')


def logout(request):
    del request.session['uid']
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        print('name, password', name, password)
        if not Manager.objects.filter(name=name).first():
            # 若该用户名不存在，则可以注册
            manager = Manager()
            manager.name = name.strip()
            manager.password = password.strip()
            manager.save()
            return HttpResponse('注册成功', status=200)
        else:
            return HttpResponse('该用户名已被注册！', status=400)

    return render(request, 'register.html')


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
    if request.method == 'POST' and request.POST.get('modify') == 'False':
        name = request.POST.get('name')
        password = request.POST.get('password')
        sex = request.POST.get('sex')
        partment = request.POST.get('partment')
        role = request.POST.get('role')

        user = User()
        user.name = name.strip()
        user.password = password.strip()
        user.sex = sex.strip()
        partment = Partment.objects.filter(name=partment.strip()).first()
        role = Role.objects.filter(name=role.strip()).first()
        if partment:
            # 如果在Partment表中查到对应部门 建立外键关系
            user.partment = partment

        if role:
            # 如果在Role表中查到对应角色 建立外键关系
            user.role = role

        user.save()

        return redirect(reverse('user_manage'))

    elif request.method == 'POST' and request.POST.get('modify') == 'True':
        id = int(request.POST.get('id'))
        name = request.POST.get('name')
        password = request.POST.get('password')
        sex = request.POST.get('sex')
        partment = request.POST.get('partment')
        role = request.POST.get('role')

        user = User.objects.get(id=id)
        # 只修改用户输入的部分
        if len(name) > 0:
            user.name = name
        if len(password) > 0:
            user.num = password
        if len(sex) > 0:
            user.num = sex
        if len(partment) > 0:
            partment = Partment.objects.filter(name=partment.strip()).first()
            if partment:
                # 如果在Partment表中查到对应部门 建立外键关系
                user.partment = partment

        if len(role) > 0:
            role = Role.objects.filter(name=role.strip()).first()
            if role:
                # 如果在Company表中查到对应公司 建立外键关系
                user.company = role

        user.save()
        return HttpResponse('修改部门信息成功', status=200)

    # 使用逻辑删除
    elif request.POST.get('delete_all') == 'False':
        id = int(request.POST.get('id'))
        user = User.objects.get(id=id)
        user.is_delete = 1
        user.save()
        return HttpResponse('企业删除成功', status=200)

    elif request.POST.get('delete_all') == 'True':
        ids = request.POST.get('ids')
        print('ids', ids)
        mod = User.objects
        if len(ids) > 1:
            ids = eval(ids)
            for id in ids:
                user = mod.get(id=id)
                user.is_delete = 1
                user.save()
        else:
            # 长度为1时单独处理
            user = mod.get(id=ids)
            user.is_delete = 1
            user.save()
        return HttpResponse('产品删除成功', status=200)

    # 如果不是POST请求，则正常显示查询到的结果
    users = User.objects.filter(is_delete=0).all()
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
    if request.method == 'POST' and request.POST.get('modify')=='False':
        num = request.POST.get('num')
        name = request.POST.get('name')

        role = Role()
        role.num = num.strip()
        role.name = name.strip()
        role.save()

        return HttpResponse('角色添加成功',status=200)

    elif request.method == 'POST' and request.POST.get('modify') == 'True':
        id = int(request.POST.get('id'))
        name = request.POST.get('name')
        num = request.POST.get('num')

        role = Role.objects.get(id=id)
        # 只修改用户输入的部分
        if len(name) > 0:
            role.name = name
        if len(num) > 0:
            role.num = num
        role.save()
        return HttpResponse('修改角色信息成功', status=200)

        # 使用逻辑删除
    elif request.POST.get('delete_all') == 'False':
        id = int(request.POST.get('id'))
        role = Role.objects.get(id=id)
        role.is_delete = 1
        role.save()
        return HttpResponse('产品删除成功', status=200)

    elif request.POST.get('delete_all') == 'True':
        ids = request.POST.get('ids')
        print('ids', ids)
        mod = Role.objects
        if len(ids) > 1:
            ids = eval(ids)
            for id in ids:
                role = mod.get(id=id)
                role.is_delete = 1
                role.save()
        else:
            # 长度为1时单独处理
            role = mod.get(id=ids)
            role.is_delete = 1
            role.save()
        return HttpResponse('产品删除成功', status=200)

    # 如果不是POST请求，则正常显示查询到的结果
    roles = Role.objects.filter(is_delete=0).all()
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
    if request.method == 'POST' and request.POST.get('modify')=='False':
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

        return HttpResponse('企业添加成功',status=200)

    elif request.method == 'POST' and request.POST.get('modify') == 'True':
        id = int(request.POST.get('id'))
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        fax = request.POST.get('fax')
        zipcode = request.POST.get('zipcode')
        site = request.POST.get('site')
        bankdeposit = request.POST.get('bankdeposit')
        banknum = request.POST.get('banknum')

        company = Company.objects.get(id=id)
        # 只修改用户输入的部分
        if len(name) > 0:
            company.name = name
        if len(phone) > 0:
            company.num = phone
        if len(fax) > 0:
            company.num = fax
        if len(zipcode) > 0:
            company.num = zipcode
        if len(site) > 0:
            company.num = site
        if len(bankdeposit) > 0:
            company.num = bankdeposit
        if len(banknum) > 0:
            company.num = banknum
        company.save()
        return HttpResponse('修改企业信息成功', status=200)

    # 使用逻辑删除
    elif request.POST.get('delete_all') == 'False':
        id = int(request.POST.get('id'))
        company = Company.objects.get(id=id)
        company.is_delete = 1
        company.save()
        return HttpResponse('企业删除成功', status=200)

    elif request.POST.get('delete_all') == 'True':
        ids = request.POST.get('ids')
        print('ids', ids)
        mod = Company.objects
        if len(ids) > 1:
            ids = eval(ids)
            for id in ids:
                company = mod.get(id=id)
                company.is_delete = 1
                company.save()
        else:
            # 长度为1时单独处理
            company = mod.get(id=ids)
            company.is_delete = 1
            company.save()
        return HttpResponse('产品删除成功', status=200)

    # 如果不是POST请求，则正常显示查询到的结果
    companys = Company.objects.filter(is_delete=0).all()
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
    if request.method == 'POST' and request.POST.get('modify')=='False':
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

        company = Company.objects.filter(name=company.strip()).first()
        prepartment = Partment.objects.filter(name=prepartment.strip()).first()
        if company:
            # 如果在Company表中查到对应公司 建立外键关系
            partment.company = company

        if prepartment:
            # 如果在Partment表中查到对应部门 建立外键关系
            partment.prepartment = prepartment

        partment.save()

        return HttpResponse('部门添加成功',status=200)

    elif request.method == 'POST' and request.POST.get('modify') == 'True':
        id = int(request.POST.get('id'))
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        fax = request.POST.get('fax')
        prepartment = request.POST.get('prepartment')
        function = request.POST.get('function')
        num = request.POST.get('num')
        company = request.POST.get('company')

        partment = Partment.objects.get(id=id)
        # 只修改用户输入的部分
        if len(name) > 0:
            partment.name = name
        if len(phone) > 0:
            partment.num = phone
        if len(fax) > 0:
            partment.num = fax
        if len(prepartment) > 0:
            prepartment = Partment.objects.filter(name=prepartment.strip()).first()
            if prepartment:
                # 如果在Partment表中查到对应部门 建立外键关系
                partment.prepartment = prepartment

        if len(function) > 0:
            partment.num = function
        if len(num) > 0:
            partment.num = num
        if len(company) > 0:
            company = Company.objects.filter(name=company.strip()).first()
            if company:
                # 如果在Company表中查到对应公司 建立外键关系
                partment.company = company

        partment.save()
        return HttpResponse('修改部门信息成功', status=200)

    # 使用逻辑删除
    elif request.POST.get('delete_all') == 'False':
        id = int(request.POST.get('id'))
        partment = Partment.objects.get(id=id)
        partment.is_delete = 1
        partment.save()
        return HttpResponse('企业删除成功', status=200)

    elif request.POST.get('delete_all') == 'True':
        ids = request.POST.get('ids')
        print('ids', ids)
        mod = Partment.objects
        if len(ids) > 1:
            ids = eval(ids)
            for id in ids:
                partment = mod.get(id=id)
                partment.is_delete = 1
                partment.save()
        else:
            # 长度为1时单独处理
            partment = mod.get(id=ids)
            partment.is_delete = 1
            partment.save()
        return HttpResponse('产品删除成功', status=200)

    # 如果不是POST请求，则正常显示查询到的结果
    partments = Partment.objects.filter(is_delete=0).all()
    pagesize = 10  # 每页显示的数据条数
    pagenum = int(request.GET.get('p', 1))  # 要显示的页码
    page, context = get_pagination_info(partments, pagesize, pagenum)  # 分页处理
    context.update({
        'the_url': reverse('user_manage'),
        'page': page
    })

    return render(request, 'system_manage/partmentManage.html', context=context)


# ============================== 删除信息 ===================================
