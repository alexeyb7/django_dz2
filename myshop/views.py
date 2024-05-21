from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from .models import Client, Product


# Create your views here.
def index(request):
    return render(request, 'myshop/index.html')


# def client_orders(request, name):
def client_orders(request):

    client = 2

    # За последние 7 дней
    last_7_days = timezone.now() - timedelta(days=7)
    client_orders_last_7_days = Product.objects.filter(order__client=client,
                                                       order__order_date__gte=last_7_days).distinct()

    # За последние 30 дней
    last_30_days = timezone.now() - timedelta(days=30)
    client_orders_last_30_days = Product.objects.filter(order__client=client,
                                                        order__order_date__gte=last_30_days).distinct()

    # За последние 365 дней
    last_365_days = timezone.now() - timedelta(days=365)
    client_orders_last_365_days = Product.objects.filter(order__client=client,
                                                         order__order_date__gte=last_365_days).distinct()

    return render(request, 'myshop/client_orders.html', {
        'client_orders_last_7_days': client_orders_last_7_days,
        'client_orders_last_30_days': client_orders_last_30_days,
        'client_orders_last_365_days': client_orders_last_365_days,
    })
