from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout

from .models import UserQuery


class ContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-inline'
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.layout = Layout('name', 'email')

    class Meta:
        model = UserQuery
