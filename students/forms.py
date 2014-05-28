from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django import forms

from .models import Student


class StudentCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""

    class Meta:
        model = Student
        fields = ('email', 'identifier', 'first_name', 'last_name', 'sex', 'university')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(StudentCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class StudentChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Student
        fields = ('email', 'password', 'identifier', 'first_name', 'last_name', 'sex', 'university')

    def clean_password(self):
        """ Regardless of what the user provides, return the initial value.
        This is done here, rather than on the field, because the
        field does not have access to the initial value
        password hash display field.
        """
        return self.initial["password"]