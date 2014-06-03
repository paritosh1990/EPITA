from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm


class CustomUserAdmin(UserAdmin):
    # The forms to add and change user instances

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference the removed 'username' field
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('name', 'user_type')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_type', 'password1', 'password2')}
        ),
    )
    list_filter = ('user_type',)
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = ('email', 'user_type')
    search_fields = ('email', )
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)