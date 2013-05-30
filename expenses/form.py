from expenses.models import Expense
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class ExpenseForm(ModelForm):
  class Meta:
    model = Expense

  def __init__(self, *args, **kwargs):
    self.helper = FormHelper()
    self.helper.form_id = 'id-expenseForm'
    self.helper.form_class = 'blueForms'
    self.helper.form_method = 'post'
    self.helper.form_action = 'submit_expense'

    self.helper.add_input(Submit('save', 'Save'))
    super(ExpenseForm, self).__init__(*args, **kwargs)

  