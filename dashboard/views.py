from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Order
from .forms import ProductForm, OrderForm
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.


@login_required
def dashboard(request):
    orders = Order.objects.all()
    products = Product.objects.all()
    staff_num = User.objects.all().count()
    product_num = Product.objects.all().count
    order_num = Order.objects.all().count
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            product_name = form.cleaned_data.get('product')
            product_quantity = form.cleaned_data.get('order_quantity')
            messages.success(
                request, f'{product_name} {product_quantity} piece make request for order!')
        form = OrderForm()
    else:
        form = OrderForm()
    context = {
        'orders': orders,
        'form': form,
        'products': products,
        'staff_num': staff_num,
        'product_num': product_num,
        'order_num': order_num,
    }
    return render(request, 'dashboard/dashboard.html', context)


@login_required
def staff(request):
    staffs = User.objects.all()
    staff_num = staffs.count()
    product_num = Product.objects.all().count
    order_num = Order.objects.all().count
    context = {
        'staff': staffs,
        'staff_num': staff_num,
        'product_num': product_num,
        'order_num': order_num,
    }
    return render(request, 'dashboard/staff.html', context)


@login_required
def staff_detail(request, id):
    primary_id = User.objects.get(pk=id)
    staff_num = User.objects.all().count()
    product_num = Product.objects.all().count
    order_num = Order.objects.all().count
    context = {
        'staffs': primary_id,
        'staff_num': staff_num,
        'product_num': product_num,
        'order_num': order_num,
    }
    return render(request, 'dashboard/staff_detail.html', context)


@login_required
def product(request):
    products = Product.objects.all()
    staff_num = User.objects.all().count()
    product_num = products.count()
    order_num = Order.objects.all().count
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            product_quantity = form.cleaned_data.get('quantity')
            messages.success(
                request, f'{product_name} {product_quantity} piece added!')
            return redirect('dashboard-product')
        form = ProductForm()
    else:
        form = ProductForm()
    context = {
        'view_product': products,
        'add_product': form,
        'staff_num': staff_num,
        'product_num': product_num,
        'order_num': order_num,
    }
    return render(request, 'dashboard/product.html', context)


@login_required
def product_edit(request, id):
    primary_id = Product.objects.get(pk=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=primary_id)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductForm(instance=primary_id)
    context = {
        'edit_product': form
    }
    return render(request, 'dashboard/products_edit.html', context)


@login_required
def product_delete(request, id):
    primary_id = Product.objects.get(pk=id)
    if request.method == 'POST':
        primary_id.delete()
        return redirect('dashboard-product')
    return render(request, 'dashboard/products_delete.html')


@login_required
def order(request):
    orders = Order.objects.all()
    staff_num = User.objects.all().count()
    product_num = Product.objects.all().count
    order_num = orders.count()
    context = {
        'orders': orders,
        'staff_num': staff_num,
        'product_num': product_num,
        'order_num': order_num,
    }
    return render(request, 'dashboard/order.html', context)
