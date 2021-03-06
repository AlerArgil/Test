import pytz
from django.apps import apps
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password

from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.translation import gettext_lazy as _

from phonenumber_field.modelfields import PhoneNumberField
from timezone_field import TimeZoneField

from core.models import IdWithPostfixModel


class CustomUserManager(UserManager):
    def _create_user(self, username, email, password, **extra_fields):
        """
        Create and save a user with the given username and password. But Exclude email
        """
        if not username:
            raise ValueError('The given username must be set')
        GlobalUserModel = apps.get_model(self.model._meta.app_label, self.model._meta.object_name)
        username = GlobalUserModel.normalize_username(username)
        user = self.model(username=username, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user


class User(AbstractUser, IdWithPostfixModel):
    """
    Client class for exercise
    """
    PRIMARY = 'prm'
    REPEATER = 'rep'
    EXTERNAL = 'ext'
    INDIRECT = 'ind'
    USER_TYPES = [
        (PRIMARY, 'Primary'),
        (REPEATER, 'Repeater'),
        (EXTERNAL, 'External'),
        (INDIRECT, 'Indirect'),
    ]

    MALE = 'm'
    FEMALE = 'f'
    UNKNOWN = 'u'
    GENDERS = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (UNKNOWN, 'Unknown'),
    ]

    POSTFIX = 1

    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
    REQUIRED_FIELDS = ['password']

    phone = PhoneNumberField(unique=True)
    first_name = models.CharField(_('first name'), max_length=150, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    middle_name = models.CharField(_('middle name'), max_length=150, blank=True)
    type = models.CharField(_('type'), choices=USER_TYPES, max_length=3)
    gender = models.CharField(_('gender'), choices=GENDERS, max_length=2)
    timezone = TimeZoneField(_('timezone'), choices_display='WITH_GMT_OFFSET', default='UTC')
    ok = models.CharField(_('ok'), max_length=150, blank=True, null=True)
    instagram = models.CharField(_('instagram'), max_length=40, blank=True, null=True)
    telegram = models.CharField(_('telegram'), max_length=40, blank=True, null=True)
    whatsapp = models.CharField(_('whatsapp'), max_length=40, blank=True, null=True)
    viber = models.CharField(_('viber'), max_length=40, blank=True, null=True)
    created_at = models.DateTimeField(_('created_at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated_at'), auto_now=True)
    email = None

    objects = CustomUserManager()


class AdditionalInfo(models.Model):
    """
    Phones, emails, social accounts. User information with Many quality
    """
    PHONE = 'p'
    EMAIL = 'e'
    VK = 'v'
    FB = 'f'
    INFO_TYPES = [
        (PHONE, 'Phone'),
        (EMAIL, 'Email'),
        (VK, 'VK'),
        (FB, 'FB'),
    ]
    user = models.ForeignKey(verbose_name=_('user'), to=User, on_delete=models.CASCADE, related_name='add_infos')
    type = models.CharField(_('type'), choices=INFO_TYPES, max_length=1)
    value = models.CharField(_('value'), max_length=50)
