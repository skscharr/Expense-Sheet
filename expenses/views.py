from django.http import HttpResponse, HttpRequest, QueryDict
from django.core.urlresolvers import reverse
from expenses.models import Expense
from django.shortcuts import render
from django.http import HttpResponseRedirect


def new(request, template='recipes/new.html'):
  expense_date = Expense.POST['date']
  expense_store = Expense.POST['store']
  expense_price = Expense.POST['price']
  expense_payment_type = Expense.POST['payment_type']
  expense_category = Expense.POST['category']

  new_expense = Expense(date=expense_date, store=expense_store, price=expense_price, 
    payment_type=expense_payment_type, category=expense_category)
  new_expense.save()

  return render(request, template)

