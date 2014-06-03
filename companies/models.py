from django.db import models

# Create your models here.

from django.conf import settings


class CompanyProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)

