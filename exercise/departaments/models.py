from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from clients.models import User
from companies.models import Company
from core.models import IdWithPostfixModel


class Departament(IdWithPostfixModel, models.Model):
    """
    Department like Law object for exercise
    """
    POSTFIX = 3
    name = models.CharField(_('name'), max_length=300)
    company = models.ForeignKey(verbose_name=_('company'), to=Company, on_delete=models.CASCADE,
                                related_name='departaments')
    users = models.ManyToManyField(verbose_name=_('users'), to=User, related_name='departaments',
                                   through='DepartamentUser', blank=True)
    families = models.ManyToManyField(verbose_name=_('families'), to='self', symmetrical=False,
                                      through='Family', through_fields=('parent', 'child'), blank=True)


class DepartamentUser(models.Model):
    """
    Many to Many table for department and user
    """
    departament = models.ForeignKey(verbose_name=_('departament'), to=Departament, on_delete=models.CASCADE,
                                    related_name='binds')
    user = models.ForeignKey(verbose_name=_('user'), to=User, on_delete=models.CASCADE, related_name='binds')
    binded_at = models.DateTimeField(verbose_name=_('binded_at'), auto_now_add=True)


class Family(models.Model):
    """
    Parent-Child relation for departaments
    """
    parent = models.ForeignKey(verbose_name=_('parent'), to=Departament, on_delete=models.CASCADE,
                               related_name='child')
    child = models.OneToOneField(verbose_name=_('child'), to=Departament, on_delete=models.CASCADE,
                                 related_name='parent', unique=True)
    level = models.PositiveSmallIntegerField(verbose_name=_('level'), default=1, validators=[MaxValueValidator(7)])

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.level = self.current_level()
        print(self.level)
        super().save(force_insert=False, force_update=False, using=None, update_fields=None)

    def clean(self):
        child_as_parent = self.__class__.objects.filter(parent=self.child).first()
        if child_as_parent and self.current_level() >= child_as_parent.level:
            raise ValidationError('Trying bind ancestors departament as child')

    def current_level(self):
        ancestor_for_current = self.__class__.objects.filter(child=self.parent).first()
        return ancestor_for_current.level + 1 if ancestor_for_current else 1
