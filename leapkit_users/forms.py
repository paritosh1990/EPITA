
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, Hidden

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """
    A form that creates a user, with no privileges, from the given email and password
    """
    def __init__(self, *args, **kargs):
        super(CustomUserCreationForm, self).__init__(*args, **kargs)
        del self.fields['username']
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Login information',
                'email',
                'password1',
                'password2',
            ),
        )

    class Meta:
        model = CustomUser


class CustomUserChangeForm(UserChangeForm):
    """
    A form that changes a user, with no privileges, from the given email and password
    """
    def __init__(self, *args, **kargs):
        super(CustomUserChangeForm, self).__init__(*args, **kargs)
        del self.fields['username']

    class Meta:
        model = CustomUser


class SignInForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(SignInForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-SignInForm'
        self.helper.form_method = 'post'
        self.helper.form_action = 'auth_view'
        self.helper.add_input(Submit('submit', 'Sign in'))