from expenses.models import Expense
from django import forms

class ExpenseForm(forms.Form):
  date = forms.DateField(USE_L10N=False)
  store = forms.CharField(min_length=1)
  price = forms.DecimalField(max_digits=20, decimal_places=2, localize=True)
  payment_type = forms.ModelChoiceField(queryset="Expenses")
  category = forms.CharField(min_length=1)


