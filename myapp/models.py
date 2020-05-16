from django.db import models
from datetime import datetime

# Create your models here.
class SalesRep(models.Model):

    POSITIONS = (
    ('junior', 'Junior'),
    ('senior', 'Senior'),
    ('manager', 'Manager')
    )

    EmployeeName = models.CharField(max_length = 50, unique=True)
    position = models.CharField(max_length = 10, choices = POSITIONS)
    commission = models.DecimalField(max_digits = 5, decimal_places = 3)

class Product(models.Model):
    name = models.CharField(max_length = 50)
    price = models.CharField(max_length = 50)

class Order(models.Model):
    ProductID = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    RepID = models.ForeignKey(SalesRep, null=True, on_delete=models.SET_NULL)
    Quantity = models.IntegerField()
    Total = models.DecimalField(max_digits=6, decimal_places=2)
    Date = models.DateTimeField(default=datetime.now())
