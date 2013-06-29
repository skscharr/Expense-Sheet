
from expenses.models import Expense
from crispy_forms.layout import *
from crispy_forms.bootstrap import *
from crispy_forms.helper import FormHelper
import floppyforms as forms

class ExpenseForm(forms.ModelForm):

  class Meta:
    model = Expense
    widgets = {
      'date': forms.DateInput,
    }

  def __init__(self, *args, **kwargs):
    self.helper = FormHelper()
    self.helper.form_id = 'id-expenseForm'
    self.helper.form_method = 'post'
    self.helper.form_class = 'form-horizontal'
    self.helper.form_action = 'submit_expense'
    self.helper.help_text_inline = True

    self.helper.layout = Layout(
      Fieldset('<h3 style="text-align:center">Expense {{expense.id}}</h3>',
        'date',
        'store', 
        PrependedText('price', '$', style='height:20px; width:175px'),
        'payment_type',
        'category', 
        style='height:20px; width:200px;',
        ),
      ),
      FormActions(
        Submit('save', 'Save'),
        Reset('reset', 'Reset'),
        ),
      )

    super(ExpenseForm, self).__init__(*args, **kwargs)

