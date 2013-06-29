from django.http import HttpResponseRedirect, HttpResponse
from chartit import PivotDataPool, PivotChart
from django.db.models import Sum
from django.shortcuts import render
from expenses.models import Expense
from expenses.form import ExpenseForm

def index(request, template='expenses/index.html'):
  all_expenses = Expense.objects.all()
  return render(request, template, {'expenses':all_expenses})

def new(request, template='expenses/new.html'):
  if request.method == 'POST':
    new_expense = ExpenseForm(request.POST)
    if new_expense.is_valid() and new_expense.clean():
      new_expense.save()
      return HttpResponseRedirect('/expenses/')
  else:
    new_expense = ExpenseForm()

  return render(request, template, {'new_expense':new_expense})

def edit(request, expense_id, template='expenses/edit.html'):
  expense = Expense.objects.get(id=expense_id)
  if request.method == 'POST':
    edit_expense = ExpenseForm(request.POST, instance=expense)
    if edit_expense.is_valid and edit_expense.clean():
      edit_expense.save()
      return HttpResponseRedirect('/expenses/')
  else:
    edit_expense = ExpenseForm(instance=expense)

  return render(request, template, {'edit_expense':edit_expense})

def delete(request, expense_id):
  if request.method == 'POST':
    expense = Expense.objects.get(id=expense_id).delete()
    return HttpResponseRedirect('/expenses/')
  else:
    return HttpResponse(status=404)

def expensePivotChart(request, template='expenses/graph.html'):
  expensepivotdata = \
    PivotDataPool( series = 
      [ {'options': {
        'source': Expense.objects.all(),
        'categories': ['store']},
      'terms': {
        'total': Sum('price'),}}
      ])

  expensepivcht = \
    PivotChart(
      datasource = expensepivotdata,
      series_options =
        [{'options': {
          'type': 'column',
          'stacking': False},
        'terms': [
          'total']}],
        chart_options = 
        { 'title': {
          'text': 'Cost by Store'},
          'xAxis': {
            'title': {
              'text': '$'}}})

  return render(request, template, {'expensepivchart': expensepivcht})