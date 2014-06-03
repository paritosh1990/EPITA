from django.db import models

from leapkit_users.models import CustomUser


class StudentProfileManager(models.Manager):
    def create_profile(self, user, first_name, last_name, sex, university):
        """
        :param user: The owner of the profile
        :param first_name: The first name of the user
        :param last_name: The last name of the user
        :param sex: The sex of the user
        :param university: The univesity the user is enrolled in
        :return: profile of the student user
        """
        profile = self.create(
            user=user,
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            university=university
        )
        return profile


class StudentProfile(models.Model):
    # Instantiating options
    KU = "KU"
    CBS = "CBS"
    DTU = "DTU"
    ITU = "ITU"
    KEA = "KEA"

    MALE = "M"
    FEMALE = "F"

    # Instantiating choice fields
    UNIVERSITIES = {
        (KU, "Copenhagen University"),
        (CBS, "Copenhagen Business School"),
        (DTU, "Danish Technical University"),
        (ITU, "IT-Universitetet"),
        (KEA, "Copenhagen School of Design and Technology"),
    }

    SEX = {
        (MALE, "Male"),
        (FEMALE, "Female"),
    }

    #Student fields
    user = models.OneToOneField(CustomUser)
    date_of_birth = models.DateField(blank=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    sex = models.CharField(max_length=3, choices=SEX, blank=True)
    university = models.CharField(max_length=3, choices=UNIVERSITIES, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    objects = StudentProfileManager()

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
        self.user.name = "%s %s" % (self.first_name, self.last_name)
        self.user.save()

        super(StudentProfile, self).save(*args, **kwargs)