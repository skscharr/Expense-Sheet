from django.http import HttpResponseRedirect
from django.shortcuts import render
from expenses.models import Expense
from expenses.form import ExpenseForm

def index(request,template='expenses/index.html'):
  all_expenses = Expense.objects.all()
  return render(request, template, {'all_expenses': all_expenses})

def new(request, template='expenses/new.html'):
  if request.method == 'POST':
    new_expense = ExpenseForm(request.POST)
    if new_expense.is_valid() and new_expense.clean():
      new_expense.save()
      return HttpResponseRedirect('/expenses/')
  else:
    new_expense = ExpenseForm()

  return render(request, template, {'new_expense':new_expense})

