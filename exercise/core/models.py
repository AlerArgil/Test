from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class IdWithPostfixModel(models.Model):
    """
    Class for add postfix in id field
    """
    POSTFIX = 0

    id = models.PositiveBigIntegerField(_('id'), primary_key=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.id:
            from core.helpers import next_id_with_postfix
            self.id = next_id_with_postfix(
                self.__class__.objects.aggregate(id_max=models.Max('id')).get('id_max', 0),
                self.POSTFIX
            )
        super().save(*args, **kwargs)

    class Meta:
        abstract = True
