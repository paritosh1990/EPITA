import floppyforms as forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm


class CompanyCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    def __init__(self, *args, **kwargs):
        super(CompanyCreationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-CompanyCreationForm'
        self.helper.form_method = 'post'
        self.helper.form_action = 'companies:profile'

        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(CompanyCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        group = Group.objects.get(name='Company')

        if commit:
            user.save()
            group.user_set.add(user)

        return user