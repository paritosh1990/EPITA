from django.contrib import admin

from .models import StudentProfile


class StudentProfileAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['user', 'first_name', 'last_name']}),
    ]

    list_display = ('first_name', 'last_name', 'university')
    search_fields = ['university', 'first_name']
    list_filter = ['university', 'sex']


admin.site.register(StudentProfile, StudentProfileAdmin)