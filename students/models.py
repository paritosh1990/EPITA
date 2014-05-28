from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class StudentManager(BaseUserManager):
    def create_user(self, email, identifier, first_name, last_name, sex, university, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            identifier=identifier,
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            university=university,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, identifier, first_name, last_name, email, sex, university, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            identifier=identifier,
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            university=university,
            password=password,
        )

        user.save(using=self._db)
        return user


class Student(AbstractBaseUser):
    #Instantiating options
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
    identifier = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    date_of_birth = models.DateField(blank=True, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    sex = models.CharField(max_length=3, choices=SEX)
    university = models.CharField(max_length=3, choices=UNIVERSITIES)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    objects = StudentManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['identifier', 'first_name', 'last_name', 'sex', 'university']

    class Meta:
        permissions = (
            ("list_projects", "Can see available projects"),
            ("view_project", "Can see detailed project"),
            ("create_project", "Can create new project"),
            ("change_project", "Can change a created project"),
            ("view_company", "Can view a company profile"),
            ("comment_project", "Can comment on a project"),
        )

    def __unicode__(self):
        return self.user_name

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def get_short_name(self):
        return self.identifier

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return False

