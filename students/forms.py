from django.contrib.auth.models import Group

import floppyforms as forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset

from custom_users.forms import CustomUserCreationForm
from custom_users.models import CustomUser


class StudentCreationForm(CustomUserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    def __init__(self, *args, **kwargs):
        super(StudentCreationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-StudentCreationForm'
        self.helper.form_method = 'post'
        self.helper.form_action = 'students:sign_up'
        self.helper.add_input(Submit('submit', 'Sign up'))
        self.helper.layout = Layout(
            Fieldset(
                '',
                'email',
                'first_name',
                'last_name',
                'password1',
                'password2',
            )
        )

    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(StudentCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.name = "%s %s" % (self.cleaned_data['first_name'], self.cleaned_data['last_name'])
        user.user_type = "STU"

        group = Group.objects.get(name='Students')

        if commit:
            user.save()
            group.user_set.add(user)

        return user