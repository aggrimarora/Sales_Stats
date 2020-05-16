from django.shortcuts import render
from django.http import HttpResponse
from .models import SalesRep, Product, Order
from datetime import datetime

# Create your views here.
def contact(request):
    return HttpResponse('contact view')

def sales(request):
    context = {
        'sales_rep' : SalesRep.objects.all(),
        'products' : Product.objects.all()
    }

    if request.method == "POST":
        time = datetime.now()
        sales_rep_id = int(request.POST.get('sales_rep'))
        lemon = int(request.POST.get('lemonade_quan'))
        orange = int(request.POST.get('orange_quan'))
        sugary = int(request.POST.get('sugary_quan'))
        ww = int(request.POST.get('whiskey_quan'))
        if lemon != 0:
            O = Order(ProductID = Product.objects.get(id=1), RepID = SalesRep.objects.get(id=sales_rep_id), Quantity = lemon, Total = 1.50 * lemon, Date = time)
            O.save()
        if orange != 0:
            O = Order(ProductID = Product.objects.get(id=2), RepID = SalesRep.objects.get(id=sales_rep_id), Quantity = orange, Total = 2.00 * lemon, Date = time)
            O.save()
        if sugary != 0:
            O = Order(ProductID = Product.objects.get(id=3), RepID = SalesRep.objects.get(id=sales_rep_id), Quantity = sugary, Total = 3.00 * lemon, Date = time)
            O.save()
        if ww != 0:
            O = Order(ProductID = Product.objects.get(id=3), RepID = SalesRep.objects.get(id=sales_rep_id), Quantity = sugary, Total = 5.50 * lemon, Date = time)
            O.save()

    return render(request, 'myapp/sales_form.html', context)
