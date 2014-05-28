from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from .models import Student
from .forms import StudentCreationForm, StudentChangeForm


class StudentAdmin(UserAdmin):
    #The forms to add and change student instances
    form = StudentChangeForm
    add_form = StudentCreationForm

    list_display = ('identifier', 'email', 'first_name', 'last_name', 'university', 'created')
    list_filter = ('university', 'sex', )

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('identifier', 'first_name', 'last_name', 'university')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('email', ' identifier', 'first_name', 'last_name', 'sex', 'university', 'password1', 'password2')
        })
    )

    search_fields = ('email', )
    ordering = ('email', )
    filter_horizontal = ()

admin.site.register(Student, StudentAdmin)
