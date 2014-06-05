from django.db import models

# Create your models here.

from custom_users.models import CustomUser


class Tag(models.Model):
    name = models.CharField(max_length=100)
    times_used = models.IntegerField(default=0)


class Project(models.Model):
    """
    This model is to be used for all projects created by both students and companies.
    It contains all the fields needed to create advanced project.
    """

    # Needed information
    SKYPE = "SKYPE"
    TELEPHONE = "TELE"
    EMAIL = "EMAIL"
    OTHER = "OTHER"

    CONTACT_OPTIONS = {
        (SKYPE, "Skype"),
        (TELEPHONE, "Telephone"),
        (EMAIL, "Email"),
        (OTHER, "Other")
    }
    contact_person = models.OneToOneField(CustomUser)
    name = models.CharField(max_length=254)
    # contact_image = models.ImageField()  # should be extracted from user
    payment = models.CharField(max_length=2, choices={("P", "Paid"), ("NP", "Not Paid")})
    project_start_date = models.DateField()
    project_end_date = models.DateField()
    students_needed = models.IntegerField()

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    preferred_type_of_contact = models.CharField(max_length=5,
                                                 choices=CONTACT_OPTIONS)

    # Other information
    BACHELOR = "BSC"
    MASTER = "MSC"
    ALL = "ALL"

    STUDENT_TYPE = {
        (BACHELOR, "Bachelor Students"),
        (MASTER, "Master Students"),
        (ALL, "All students")
    }

    # project_image = models.ImageField()
    #project_document = models.FileField()
    course_requirements = models.CharField(null=True,
                                           max_length=150,
                                           help_text="This field indicates if the "
                                                     "project only applies to some courses")
    region_requirements = models.CharField(null=True,
                                           max_length=100,
                                           help_text="This field indicates if the project"
                                                     "only applies to some regions")
    country_requirements = models.CharField(null=True,
                                            max_length=30,
                                            help_text="This field is used to indicate if the project"
                                                      "only applies to some countries")
    education_requirements = models.CharField(max_length=3,
                                              choices=STUDENT_TYPE,
                                              default=ALL,
                                              help_text="This field indicates if a certain education level is required")

    university_requirements = models.CommaSeparatedIntegerField(max_length=50)
    future_employment = models.BooleanField(default=False)

    web_page = models.URLField()
    nda_required = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="project_tag")

    def __unicode__(self):
        return self.name





