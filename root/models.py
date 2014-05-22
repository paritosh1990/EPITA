from django.db import models


# Create your models here.

class TimeStampedModel(models.Model):
	"""
	An abstract base class model that provides self-updating 'created' and 'modified' fields
	"""
	created 			= models.DateTimeField(auto_now_add=True)
	modified			= models.DateTimeField(auto_now_add=True)


	class Meta:
		abstract = True


class Question(TimeStampedModel):
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

class UserQuery(TimeStampedModel):
	name 		= models.CharField(max_length=2500, blank=True, default='')
	email 		= models.EmailField(max_length=100, unique=True)
	subject 	= models.CharField(max_length=200)
	body		= models.TextField()
	answer 		= models.TextField()

	def __unicode__(self):
		return self.subject
