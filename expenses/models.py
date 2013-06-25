from django.db import models
from django.db.models import Sum
from django.utils import timezone
import datetime

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

  def __unicode__(self):
    return u'%s' % (self.date)

  #Expense.objects.aggregate(total_price = Sum('price'))
  def _price_sum(self):
    return self.objects.aggregate(total_price = Sum('price'))['total_price']

  price_sum = property(_price_sum)