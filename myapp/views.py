from django.shortcuts import render
from django.http import HttpResponse
from .models import SalesRep, Product, Order
from datetime import datetime
from .forms import ReportForm
from django.contrib import messages

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
        cart = request.POST.get('order')
        amount = float(request.POST.get('total'))
        print(request.POST)
        #checks if order amount > 0
        if amount > 0:
            O = Order(RepID = SalesRep.objects.get(id=sales_rep_id), List = cart, Total = amount, Date = time)
            O.save()
            messages.success(request, "Your Order has been saved successfully")
        else:
            messages.add_message(request, messages.ERROR, "Your Cart is empty.")

    return render(request, 'myapp/sales_form.html', context)

def report(request):
    report = None
    c = None
    earned = 0.00
    total_amount = 0.00
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ReportForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            start = form.cleaned_data['Start_Date']
            end = form.cleaned_data['End_Date']
            id = form.cleaned_data['RepID']
            print(request.POST)
            #gets the required queries for the report
            q = Order.objects.filter(Date__date__gte = start, Date__date__lte = end, RepID = id)
            for query in q:
                total_amount = total_amount + float(query.Total)
                earned = earned + ((float(id.commission)/100) * float(query.Total))
            earned = round(earned, 2)
            c = (float(id.commission)/100)
            report = q
            messages.success(request, "Successfully Generated report for " + id.EmployeeName)
        else:
            # Append css class to every field that contains errors.
            for field in form.errors:
                form[field].field.widget.attrs['class'] = 'error'

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ReportForm()

    return render(request, 'myapp/sales_report.html', {'form' : form , 'report' : report, 'com' : c, 'total' : earned, 'total_price' : total_amount})
