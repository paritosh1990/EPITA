from django.test 					import TestCase
from django.contrib.auth.models 	import User
from django.core.urlresolvers 		import reverse

from .models 					import Question


class QuestionTests(TestCase):

	def setUp(self):
		self.user = User.objects.create(username="test")

	def create_question(question="Test Question", answer="42", subject="S"):
		return Question.objects.create(
			question 	= question,
			answer 		= answer,
			subject 	= subject
		)

	def test_question_creation(self):
		question = self.create_question()

		self.assertTrue(isinstance(question, Question))
		self.assertEquals(question.__unicode__(), question.question)

		