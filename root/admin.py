from django.contrib import admin

from .models import Question

class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, 	 	{'fields': ['question', 'answer', 'subject']}),
	]

	list_display 	= ('question', 'answer','subject')
	search_fields 	= ['question']
	list_filter 	= ['subject']

admin.site.register(Question, QuestionAdmin)