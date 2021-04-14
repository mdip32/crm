from django.shortcuts import render
from .models import *


# Create your views here.

def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_orders = orders.count()
    total_delivered = orders.filter(status='Delivered').count()
    total_pending = orders.filter(status='Pending').count()

    context = {
        'orders': orders,
        'customers': customers,
        'total_orders': total_orders,
        'total_delivered': total_delivered,
        'total_pending': total_pending,
    }

    return render(request, 'accounts/dashboard.html', context)


def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': products})


def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    order_count = orders.count()
    contex = {
        'customer': customer,
        'orders': orders,
        'order_count': order_count,
    }
    return render(request, 'accounts/customer.html', contex)
