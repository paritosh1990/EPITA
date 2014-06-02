from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.core.mail import send_mail
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given email and password
        :param email: Text
        :param password: Text
        :param is_staff: Boolean
        :param is_superuser: Boolean
        :param extra_fields: All extra fields needed to extend the model.
        :return: User
        """
        now = timezone.now()

        if not email:
            raise ValueError("The email has to be set")

        email = self.normalize_email(email)

        user = self.model(
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a User with the given email and password
        :param email: Text
        :param password: Text
        :param extra_fields: All extra fields needed to extend the model.
        :return: User
        """
        return self._create_user(email=email, password=password, is_staff=False, is_superuser=False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password
        :param email: Text
        :param password: Text
        :param extra_fields: All extra fields needed to extend the model.
        :return: User
        """
        return self._create_user(email=email, password=password, is_staff=True, is_superuser=True, **extra_fields)


class CustomUser(PermissionsMixin, AbstractBaseUser):
    """
    User is the new base for all users of the system, both internally in Leapkit and normal external users
    """
    username = models.CharField(max_length=254, blank=True)
    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=254, blank=True)
    last_name = models.CharField(max_length=254, blank=True)
    address_1 = models.CharField(max_length=254, blank=True)
    address_2 = models.CharField(max_length=254, blank=True)
    area_code = models.CharField(max_length=20, blank=True)
    country_code = models.CharField(max_length=10, blank=True)

    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin '
                                               'site.'))
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_('Designates whether this user should be treated as '
                                                'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'address_1', 'address_2', 'area_code', 'country_code']

    objects = CustomUserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_absolute_url(self):
        """
        :return: An url being in the format users/username
        """
        return "/users/%s/" % urlquote(self.get_url_name())

    def get_full_name(self):
        """
        :return: First name + last name, with a space in between
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """
        :return: Username
        """
        return self.username

    def get_url_name(self):
        url = "%s_%s" % (self.first_name, self.last_name)
        return url.strip()

    def email_user(self, subject, message, from_email=None):
        """
        This method is used to make it easy to communicate with all users via mail
        :param subject: The subject of the email
        :param message: The message intended for the user
        :param from_email: An email to which the user can reply to.
        :return: Nothing
        """
        send_mail(subject=subject, message=message, from_email=from_email, recipient_list=[self.email])