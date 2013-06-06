from expenses.models import Expense
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Button, Field
from crispy_forms.bootstrap import FormActions, PrependedText
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
    self.helper.form_class = 'form-horizontal'
    self.helper.form_method = 'post'
    self.helper.form_action = 'submit_expense'

    self.helper.layout = Layout(
      Field('date'),
      Field('store'),
      PrependedText( 'price', '$'),
      Field('payment_type'),
      Field('category'),
      FormActions(
        Submit('save', 'Save'),
        Button('cancel', 'Cancel'),
        ),
    )
    super(ExpenseForm, self).__init__(*args, **kwargs)
