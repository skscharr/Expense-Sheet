from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from expenses.models import Expense
from django.utils import timezone

urlpatterns = patterns('',
  url(r'^$', 
    ListView.as_view(
      queryset=Expense.objects.filter(date__lte=timezone.now) \
          .order_by('-date')[:5],
      context_object_name='expenses',
      template_name='expenses/index.html'),
    name='index'),
  )