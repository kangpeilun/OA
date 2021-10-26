from django.shortcuts import render, reverse, HttpResponse, redirect
from django.core.paginator import Paginator, Page

from customer_manage.models import Customer, Product
from utils.paginator import get_pagination_info
from utils.authorization import is_authorized

# Create your views here.

# ============================== 弹出页 ===================================
def customer_show(request):
    id = int(request.GET.get('id'))
    customer = Customer.objects.get(id=id)
    context = {
        'customer': customer
    }
    return render(request, 'customer_manage/customerShow.html', context=context)


def product_show(request):
    id = int(request.GET.get('id'))
    product = Product.objects.get(id=id)

    context = {
        'product': product
    }
    return render(request, 'customer_manage/productShow.html', context=context)

# ============================== 客户信息管理 ===================================
def customer_manage(request):
    manager, authoried = is_authorized(request)
    # 如果没有被授权，则将重定向到登陆页面
    if not authoried:
        return redirect(reverse('login'))

    # 如果是post请求，则添加用户信息
    if request.method == 'POST' and request.POST.get('modify')=='False':
        name = request.POST.get('name')
        briefinfo = request.POST.get('briefinfo')
        area = request.POST.get('area')
        type = request.POST.get('type')
        nature = request.POST.get('nature')
        describe = request.POST.get('describe')

        customer = Customer()
        customer.name = name.strip()
        customer.briefinfo = briefinfo.strip()
        customer.area = area.strip()
        customer.type = type.strip()
        customer.nature = nature.strip()
        customer.describe = describe.strip()

        customer.save()

        HttpResponse('修改客户信息成功', status=200)

    elif request.method == 'POST' and request.POST.get('modify')=='True':
        id = int(request.POST.get('id'))
        name = request.POST.get('name')
        briefinfo = request.POST.get('briefinfo')
        area = request.POST.get('area')
        type = request.POST.get('type')
        nature = request.POST.get('nature')
        describe = request.POST.get('describe')

        customer = Customer.objects.get(id=id)
        # 只修改用户输入的部分
        if len(name)>0:
            customer.name = name
        if len(briefinfo)>0:
            customer.supplier = briefinfo
        if len(area) > 0:
            customer.num = area
        if len(type)>0:
            customer.type = type
        if len(nature)>0:
            customer.price = nature
        if len(describe)>0:
            customer.describe = describe
        customer.save()
        return HttpResponse('修改客户信息成功', status=200)

        # 使用逻辑删除
    elif request.POST.get('delete_all') == 'False':
        id = int(request.POST.get('id'))
        customer = Customer.objects.get(id=id)
        customer.is_delete = 1
        customer.save()
        return HttpResponse('产品删除成功', status=200)

    elif request.POST.get('delete_all') == 'True':
        ids = request.POST.get('ids')
        print('ids', ids)
        mod = Customer.objects
        if len(ids) > 1:
            ids = eval(ids)
            for id in ids:
                customer = mod.get(id=id)
                customer.is_delete = 1
                customer.save()
        else:
            # 长度为1时单独处理
            customer = mod.get(id=ids)
            customer.is_delete = 1
            customer.save()
        return HttpResponse('产品删除成功', status=200)

    if request.GET.get('search') == 'True':
        # TODO: 查询有些未知的问题
        pass

    # 如果不是POST请求，则正常显示查询到的结果
    customers = Customer.objects.filter(is_delete=0).all()
    pagesize = 10  # 每页显示的数据条数
    pagenum = int(request.GET.get('p', 1))  # 要显示的页码
    page, context = get_pagination_info(customers, pagesize, pagenum)  # 分页处理
    context.update({
        'the_url': reverse('customer_manage'),
        'page': page
    })

    return render(request, 'customer_manage/customerManage.html', context=context)


# ============================== 产品信息管理 ===================================
def product_manage(request):
    manager, authoried = is_authorized(request)
    # 如果没有被授权，则将重定向到登陆页面
    if not authoried:
        return redirect(reverse('login'))

    # 如果是post请求，则添加用户信息
    if request.method == 'POST' and request.POST.get('modify')=='False':
        name = request.POST.get('name')
        supplier = request.POST.get('supplier')
        num = request.POST.get('num')
        type = request.POST.get('type')
        price = request.POST.get('price')
        describe = request.POST.get('describe')

        product = Product()
        product.name = name.strip()
        product.supplier = supplier.strip()
        product.num = num.strip()
        product.type = type.strip()
        product.price = price.strip()
        product.describe = describe.strip()
        product.save()
        return HttpResponse('添加产品成功', status=200)

    elif request.method == 'POST' and request.POST.get('modify')=='True':
        id = int(request.POST.get('id'))
        name = request.POST.get('name')
        supplier = request.POST.get('supplier')
        num = request.POST.get('num')
        type = request.POST.get('type')
        price = request.POST.get('price')
        describe = request.POST.get('describe')

        product = Product.objects.get(id=id)
        # 只修改用户输入的部分
        if len(name)>0:
            product.name = name
        if len(supplier)>0:
            product.supplier = supplier
        if len(num) > 0:
            product.num = num
        if len(type)>0:
            product.type = type
        if len(price)>0:
            product.price = price
        if len(describe)>0:
            product.describe = describe
        product.save()
        return HttpResponse('修改产品信息成功', status=200)

    # 使用逻辑删除
    elif request.POST.get('delete_all')=='False':
        id = int(request.POST.get('id'))
        product = Product.objects.get(id=id)
        product.is_delete = 1
        product.save()
        return HttpResponse('产品删除成功', status=200)

    elif request.POST.get('delete_all')=='True':
        ids = request.POST.get('ids')
        print('ids', ids)
        mod = Product.objects
        if len(ids)>1:
            ids = eval(ids)
            for id in ids:
                product = mod.get(id=id)
                product.is_delete=1
                product.save()
        else:
            # 长度为1时单独处理
            product = mod.get(id=ids)
            product.is_delete = 1
            product.save()
        return HttpResponse('产品删除成功', status=200)

    if request.GET.get('search')=='True':
        # TODO: 查询有些未知的问题
        pass

    # 如果不是POST请求，则正常显示查询到的结果
    products = Product.objects.filter(is_delete=0).all()
    pagesize = 10  # 每页显示的数据条数
    pagenum = int(request.GET.get('p', 1))  # 要显示的页码
    page, context = get_pagination_info(products, pagesize, pagenum)  # 分页处理
    context.update({
        'the_url': reverse('product_manage'),
        'page': page
    })

    return render(request, 'customer_manage/productManage.html', context=context)


# ============================== 删除信息 ===================================
# TODO: 使用一个视图函数控制所有的表的删除, 可以实现批量删除
def delete_info(request):
    pass
