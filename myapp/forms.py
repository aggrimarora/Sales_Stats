from django import forms
from django.forms import ModelForm
from .models import Order, SalesRep

class DateInput(forms.DateInput):
    input_type = 'date'

class ReportForm(ModelForm):
    error_css_class = 'error'
    Start_Date = forms.DateField(widget=DateInput)
    End_Date = forms.DateField(widget=DateInput)
    class Meta:
        model = Order
        fields = ['RepID']
