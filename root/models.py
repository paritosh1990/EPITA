import datetime

from django.db import models
from django.utils import timezone


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating 'created' and 'modified' fields
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class AnswersModel(TimeStampedModel):
    has_been_answered = models.BooleanField(default=False)
    answer = models.TextField(default='')

    class Meta:
        abstract = True


class Question(TimeStampedModel):
    STUDENTS = 'S'
    COMPANIES = 'C'
    UNIVERSITIES = 'U'

    QUESTION_SUBJECT_AREA = (
        (STUDENTS, 'Students'),
        (COMPANIES, 'Companies'),
        (UNIVERSITIES, 'Universities'),
    )

    question = models.CharField(max_length=200)
    answer = models.TextField()
    subject = models.CharField(max_length=1,
                               choices=QUESTION_SUBJECT_AREA,
                               default=STUDENTS)

    def __unicode__(self):
        return self.question

    class Meta:
        ordering = ["subject", "question"]
        verbose_name_plural = "Frequently Asked Questions"


class UserQuery(TimeStampedModel):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    body = models.TextField()

    def __unicode__(self):
        return self.name

    def was_asked_recently(self):
        now = timezone.now()

        return now - datetime.timedelta(days=1) <= self.created < now

    was_asked_recently.admin_order_field = 'created'
    was_asked_recently.boolean = True
    was_asked_recently.short_description = 'Question asked recently?'

    class Meta:
        ordering = ["created"]
        verbose_name_plural = "User Queries"
