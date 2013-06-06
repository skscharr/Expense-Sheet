from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Expense(models.Model):
  PAYMENT_CHOICES = (
    ('Cash', 'cash'), 
    ('Credit', 'credit'),
    ('Debit', 'debit')
    )
  date = models.DateField()
  store = models.CharField(max_length=100)
  price = models.DecimalField(max_digits=20, decimal_places=2)
  payment_type = models.CharField(max_length=8, choices=PAYMENT_CHOICES)
  category = models.CharField(max_length=100)

