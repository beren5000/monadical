from django.db import models

from django.db import models
from django.utils.translation import gettext_lazy as _


class KeyValue(models.Model):
    """Key Value object to fulfill the requirement on Monadical Test"""
    key = models.CharField(max_length=225,unique=True, verbose_name=_('key'), help_text=_('key'))
    value = models.CharField(max_length=225, verbose_name=_('value'), help_text=_('value'))

    class Meta:
        verbose_name = _('Key Value Object')
        verbose_name_plural = _('Key Value Objects')

