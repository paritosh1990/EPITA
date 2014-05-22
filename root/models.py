from django.db import models


# Create your models here.


class Question(models.Model):
	STUDENTS 		= 'S'
	COMPANIES 		= 'C'
	UNIVERSITIES 	= 'U'
	
	QUESTION_SUBJECT_AREA = (
	    (STUDENTS, 'Students'),
	    (COMPANIES, 'Companies'),
	    (UNIVERSITIES, 'Universities'),
	)

	question 	= models.CharField(max_length=200)
	answer 		= models.TextField()
	subject 	= models.CharField(max_length=1,
                                      choices=QUESTION_SUBJECT_AREA,
                                      default=STUDENTS)

	def __unicode__(self):
		return self.question

	class Meta:
		ordering = ["subject", "question"]
	