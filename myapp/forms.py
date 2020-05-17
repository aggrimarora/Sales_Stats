from django import forms
from django.forms import ModelForm
from .models import Order, SalesRep

class DateInput(forms.DateInput):
    input_type = 'date'

class ReportForm(ModelForm):
    error_css_class = 'error'
    Start_Date = forms.DateField(widget=DateInput(attrs={'class':''}))
    End_Date = forms.DateField(widget=DateInput(attrs={'class':''}))
    class Meta:
        model = Order
        fields = ['RepID']

    def clean(self):
        form_data = self.cleaned_data
        start = form_data['Start_Date']
        end = form_data['End_Date']
        if start > end:
            self._errors["Start_Date"] = ["Start Date should be before the End Date"]
        return form_data
