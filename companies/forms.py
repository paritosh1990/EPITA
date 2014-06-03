from django.contrib.auth.models import Group

import floppyforms as forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset

from custom_users.forms import CustomUserCreationForm
from custom_users.models import CustomUser


class CompanyCreationForm(CustomUserCreationForm):
    company_name = forms.CharField(required=True)

    def __init__(self, *args, **kwargs):
        super(CompanyCreationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-CompanyCreationForm'
        self.helper.form_method = 'post'
        self.helper.form_action = 'companies:sign_up'
        self.helper.layout = Layout(
            Fieldset(
                '',
                'email',
                'company_name',
                'password1',
                'password2',
            )
        )
        self.helper.add_input(Submit('submit', 'SIGN UP'))

    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(CompanyCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.name = self.cleaned_data['company_name']
        user.user_type = "COM"

        group = Group.objects.get(name='Companies')

        if commit:
            user.save()
            group.user_set.add(user)

        return user