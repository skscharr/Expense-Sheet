from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.edit import UpdateView, DeleteView
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

def edit(request, expense_id, template='expenses/new.html'):
  expense = Expense.objects.get(id=expense_id)
  if request.method == 'POST':
    form = ExpenseForm(request.post, instance=expense)
    if form.is_valid and form.clean():
      expense = form.save()
      return HttpResponseRedirect('/expenses/')
    else:
      form = ExpenseForm(instance=expense)

def delete(request, expense_id):
  if request.method == 'POST':
    expense = Expense.objects.get(id=expense_id).delete()
    return HttpResponseRedirect('/expenses/')
  else:
    return HttpResponse(status=404)