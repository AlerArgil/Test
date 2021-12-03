from django.core.validators import MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from clients.models import User
from core.models import IdWithPostfixModel


class Departament(IdWithPostfixModel, models.Model):
    """
    Department like Law object for exercise
    """
    POSTFIX = 3
    name = models.CharField(_('name'), max_length=300)
    level = models.PositiveSmallIntegerField(_('level'), default=0, validators=[MaxValueValidator(7)])
    users = models.ManyToManyField(verbose_name=_('users'), to=User, related_name='departaments', through='DepartamentUser')


class DepartamentUser(models.Model):
    """
    Many to Many table for department and user
    """
    departament = models.ForeignKey(verbose_name=_('departament'), to=Departament, on_delete=models.CASCADE,
                                    related_name='binds')
    user = models.ForeignKey(verbose_name=_('user'), to=User, on_delete=models.CASCADE, related_name='binds')
    binded_at = models.DateTimeField(_('binded_at'), auto_now_add=True)
