from django.contrib import admin

from .models import Question, UserQuery


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question', 'answer', 'subject']}),
    ]

    list_display = ('question', 'answer', 'subject')
    search_fields = ['question']
    list_filter = ['subject']


admin.site.register(Question, QuestionAdmin)


class UserQueryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'email', 'body', 'has_been_answered', 'answer']}),
    ]

    list_display = ('name', 'email', 'has_been_answered')
    list_filter = ['has_been_answered', 'created']


admin.site.register(UserQuery, UserQueryAdmin)
