from django.contrib import admin
from expenses.models import Expense
from django.utils import timezone
import datetime

class ExpenseAdmin(admin.ModelAdmin):
  fieldsets = [
    ('Date', {'fields': ['date']}),
    ('Store', {'fields': ['store']}),
    ('Price', {'fields': ['price']}),
    ('Payment Type', {'fields': ['payment_type']}),
    ('Category', {'fields': ['category']}),
  ]
  search_fields = ['date', 'store', 'payment_type', 'category']
  list_display = ['date', 'store', 'payment_type', 'category']
  list_filter = ['date', 'store', 'payment_type', 'category']
  date_hierarchy = 'date'

admin.site.register(Expense, ExpenseAdmin)