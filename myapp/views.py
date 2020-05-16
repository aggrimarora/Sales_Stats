from django.shortcuts import render
from django.http import HttpResponse
from .models import SalesRep, Product, Order

# Create your views here.
def contact(request):
    return HttpResponse('contact view')

def sales(request):
    if request.method == "POST":
        print(request.POST)

    context = {
        'sales_rep' : SalesRep.objects.all(),
        'products' : Product.objects.all()
    }
    return render(request, 'myapp/sales_form.html', context)
