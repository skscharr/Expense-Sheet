from django.db import models
from django.db.models import Sum
from django.utils import timezone
import datetime


class ExpenseManager(models.Manager):
  def price_sum(self):
    #Expense.objects.aggregate(total_price = Sum('price'))
    return super(ExpenseManager, self).aggregate(total_price = Sum('price'))['total_price']

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
  objects = models.Manager()
  price_object = ExpenseManager()

  def __unicode__(self):
    return u'%s' % (self.date)
