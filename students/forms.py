from django.contrib.auth.models import Group

import floppyforms as forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset

from custom_users.forms import CustomUserCreationForm
from custom_users.models import CustomUser
from models import StudentProfile


class StudentCreationForm(CustomUserCreationForm):
    # Instantiating options
    KU = "KU"
    CBS = "CBS"
    DTU = "DTU"
    ITU = "ITU"
    KEA = "KEA"

    MALE = "M"
    FEMALE = "F"

    # Instantiating choice fields
    UNIVERSITIES = {
        (KU, "Copenhagen University"),
        (CBS, "Copenhagen Business School"),
        (DTU, "Danish Technical University"),
        (ITU, "IT-Universitetet"),
        (KEA, "Copenhagen School of Design and Technology"),
    }

    SEX = {
        (MALE, "Male"),
        (FEMALE, "Female"),
    }

    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    sex = forms.ChoiceField(widget=forms.RadioSelect, choices=SEX)
    university = forms.ChoiceField(choices=UNIVERSITIES)

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
                'sex',
                'password1',
                'password2',
                'university',
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
            StudentProfile.objects.get_or_create(user=user,
                                                 first_name=self.cleaned_data['first_name'],
                                                 last_name=self.cleaned_data['last_name'],
                                                 sex=self.cleaned_data['sex'],
                                                 university=self.cleaned_data['university'])

        return user