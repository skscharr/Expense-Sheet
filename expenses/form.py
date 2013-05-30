from expenses.models import Expense
from django.utils import timezone
from django.forms import ModelForm
from django import forms
import datetime

class ExpenseForm(ModelForm):
  class Meta:
    model = Expense

'''class ExpenseForm(forms.Form):
  date = forms.DateField()
  store = forms.CharField(min_length=1)
  price = forms.DecimalField(max_digits=20, decimal_places=2, localize=True)
  payment_type = forms.ModelChoiceField(queryset="Expenses")
  category = forms.CharField(min_length=1)'''
  