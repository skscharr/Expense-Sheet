from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Sum
from django.shortcuts import render
from expenses.models import Expense
from expenses.form import ExpenseForm

def index(request, template='expenses/index.html'):
  all_expenses = Expense.objects.all()
  return render(request, template)

def new(request, template='expenses/new.html'):
  if request.method == 'POST':
    new_expense = ExpenseForm(request.POST)
    if new_expense.is_valid() and new_expense.clean():
      new_expense.save()
      return HttpResponseRedirect('/')     
  else:
    new_expense = ExpenseForm()

  return render(request, template, {'new_expense':new_expense})

def edit(request, expense_id, template='expenses/edit.html'):
  expense = Expense.objects.get(id=expense_id)
  if request.method == 'POST':
    edit_expense = ExpenseForm(request.POST, instance=expense)
    if edit_expense.is_valid:
      edit_expense.save()
      return HttpResponseRedirect('/')
  else:
    edit_expense = ExpenseForm(instance=expense)

  return render(request, template, {'edit_expense':edit_expense})

def delete(request, expense_id):
  if request.method == 'POST':
    expense = Expense.objects.get(id=expense_id).delete()
    return HttpResponseRedirect('/')
  else:
    return HttpResponse(status=404)
