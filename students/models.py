from django.db import models


class StudentProfile(models.Model):
    # Instantiating options
    KU = "KU"
    CBS = "CBS"
    DTU = "DTU"
    ITU = "ITU"
    KEA = "KEA"

    MALE = "M"
    FEMALE = "F"

    #Instantiating choice fields
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
    date_of_birth = models.DateField(blank=True, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    sex = models.CharField(max_length=3, choices=SEX)
    university = models.CharField(max_length=3, choices=UNIVERSITIES)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        permissions = (
            ("list_projects", "Can see available projects"),
            ("view_project", "Can see detailed project"),
            ("create_project", "Can create new project"),
            ("change_project", "Can change a created project"),
            ("view_company", "Can view a company profile"),
            ("comment_project", "Can comment on a project"),
        )

