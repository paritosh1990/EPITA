from django.contrib import admin

from .models import Question, UserQuery

class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, 	 	{'fields': ['question', 'answer', 'subject']}),
	]

	list_display 	= ('question', 'answer','subject')
	search_fields 	= ['question']
	list_filter 	= ['subject']

admin.site.register(Question, QuestionAdmin)

class UserQueryAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, 	 	{'fields': ['name', 'email', 'body']}),
	]

	list_display 	= ('name', 'email')
	list_filter 	= ['created']


admin.site.register(UserQuery, UserQueryAdmin)
