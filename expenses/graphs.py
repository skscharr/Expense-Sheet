from chartit import PivotDataPool, PivotChart
from expenses.models import Expense

def expensePivotChart(request):
  expensepivotdata = \
    PivotDataPool( series = 
      [ {'options': {
        'source': Expense.objects.all()
        'categories': ['store']},
      'terms': {
        'total': Sum('price'),
        'legend_by': ['store'],
        'top_n_per_cat': 1000000}}
      ])

  expensepivcht = \
    PivotChart(
      datasource = expensepivotdata,
      series_options =
        [{'options': {
          'type': 'column',
          'stacking': False},
        'terms': [
          'sum_price']}],
        chart_options = 
        { 'title': {
          'text': 'Cost by Store'},
          'xAxis': {
            'title': {
              'text': '$'}}})

  return render_to_response({'expensepivchart': expensepivcht})