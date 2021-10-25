from django.shortcuts import render, reverse, HttpResponse, redirect

from customer_manage.models import Customer, Product
from utils.paginator import get_pagination_info
from utils.authorization import is_authorized

# Create your views here.

# ============================== 客户信息管理 ===================================
def customer_manage(request):
    manager, authoried = is_authorized(request)
    # 如果没有被授权，则将重定向到登陆页面
    if not authoried:
        return redirect(reverse('login'))

    # 如果是post请求，则添加用户信息
    if request.method == 'POST':
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

        return redirect(reverse('customer_manage'))

    # 如果不是POST请求，则正常显示查询到的结果
    customers = Customer.objects.all()
    pagesize = 10  # 每页显示的数据条数
    pagenum = int(request.GET.get('p', 1))  # 要显示的页码
    page, context = get_pagination_info(customers, pagesize, pagenum)  # 分页处理
    context.update({
        'the_url': reverse('user_manage'),
        'page': page
    })

    return render(request, 'customer_manage/customerManage.html', context=context)


# ============================== 产品信息管理 ===================================
def product_manage(request):
    manager, authoried = is_authorized(request)
    # 如果没有被授权，则将重定向到登陆页面
    if not authoried:
        return redirect(reverse('login'))

    print(request.path_info)
    # 如果是post请求，则添加用户信息
    if request.method == 'POST':
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

        return redirect(reverse('product_manage'))

    # 如果不是POST请求，则正常显示查询到的结果
    products = Product.objects.all()
    pagesize = 10  # 每页显示的数据条数
    pagenum = int(request.GET.get('p', 1))  # 要显示的页码
    page, context = get_pagination_info(products, pagesize, pagenum)  # 分页处理
    context.update({
        'the_url': reverse('user_manage'),
        'page': page
    })

    return render(request, 'customer_manage/productManage.html', context=context)


# ============================== 删除信息 ===================================
# TODO: 使用一个视图函数控制所有的表的删除, 可以实现批量删除
def delete_info(request):
    pass
