from django.db import models

# Create your models here.

from django.conf import settings


class CompanyProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    address = models.CharField(max_length=254)
    number_of_employees = models.IntegerField()
    region = models.CharField(max_length=254)
    country = models.CharField(max_length=100)
    description = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.user.get_full_name()

    def save(self, *args, **kwargs):
        # self.user.name = "%s %s" % (self.first_name, self.last_name)
        # self.user.save()

        super(CompanyProfile, self).save(*args, **kwargs)
