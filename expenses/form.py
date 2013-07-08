
from expenses.models import Expense
from crispy_forms.layout import *
from crispy_forms.bootstrap import *
from crispy_forms.helper import FormHelper
import floppyforms as forms

class ExpenseForm(forms.ModelForm):

  class Meta:
    model = Expense
    fields = ['date', 'store', 'price', 'payment_type', 'category']
    widgets = {
      'date': forms.DateInput,
    }

  def __init__(self, *args, **kwargs):
    self.helper = FormHelper()
    self.helper.form_id = 'id-expenseForm'
    self.helper.form_method = 'POST'
    self.helper.form_class = 'form-horizontal'
    self.helper.form_action = '#'
    self.helper.help_text_inline = True

    self.helper.layout = Layout(
      Fieldset(
        '',
        'date',
        'store', 
        'price', 
        'payment_type',
        'category', 
        ),
      FormActions(
        Submit('save', 'Save'),
        Reset('reset', 'Reset'),
        )
      )
    super(ExpenseForm, self).__init__(*args, **kwargs)

