from django.urls import path
from . import views

urlpatterns = [

    path('sales/form', views.sales),
    path('sales/report', views.report)
]
