from django.db import models

from custom_users.models import CustomUser


class University(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    number_of_students = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name


class StudentProfile(models.Model):
    # Instantiating options

    MALE = "M"
    FEMALE = "F"

    SEX = {
        (MALE, "Male"),
        (FEMALE, "Female"),
    }

    # Student fields
    user = models.OneToOneField(CustomUser)
    date_of_birth = models.DateField(null=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    sex = models.CharField(max_length=3, choices=SEX, blank=True)
    university = models.ForeignKey(University)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.user.get_full_name()

    class Meta:
        permissions = (
            ("list_projects", "Can see available projects"),
            ("view_project", "Can see detailed project"),
            ("create_project", "Can create new project"),
            ("change_project", "Can change a created project"),
            ("view_company", "Can view a company profile"),
            ("comment_project", "Can comment on a project"),
        )

    def save(self, *args, **kwargs):
        # self.user.name = "%s %s" % (self.first_name, self.last_name)
        # self.user.save()

        super(StudentProfile, self).save(*args, **kwargs)

