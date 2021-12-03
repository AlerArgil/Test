from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import IdWithPostfixModel


class Company(IdWithPostfixModel, models.Model):
    """
    Company like Law object for exercise
    """
    POSTFIX = 2
    full_name = models.CharField(_('full name'), max_length=300)
    cut_name = models.CharField(_('cut name'), max_length=150)
    inn = models.CharField(_('INN'), max_length=12)
    kpp = models.CharField(_('KPP'), max_length=9)
    created_at = models.DateTimeField(_('created_at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated_at'), auto_now=True)
