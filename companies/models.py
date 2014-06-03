from django.db import models

# Create your models here.

from leapkit_users.models import CustomUser


class CompanyProfile(models.Model):
    user = models.OneToOneField(CustomUser)

