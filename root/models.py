from django.db import models

# Create your models here.


class Question(models.Model):
	question 	= models.CharField(max_length=200)
	answer 		= models.TextField()

	def __unicode__(self):
		return self.question
	