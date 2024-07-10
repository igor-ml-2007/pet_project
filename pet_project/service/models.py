from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey
from common.models import Media
from common.utils import validate_phone_number
from ckeditor.fields import RichTextField


class AboutService(models.Model):
    title = models.CharField(max_length=120, verbose_name=_('title'))
    image = models.ForeignKey(Media, on_delete=models.CASCADE, verbose_name=_('image'))
    advantages = models.CharField(max_length=120, verbose_name=_('advantages'))
    desc = models.TextField(_('description'))

    class Meta:
        verbose_name = _('About Service')
        verbose_name_plural = _('About Services')

    def __str__(self):
        return self.title


class WhatWeRepair(models.Model):
    image = models.ForeignKey(Media, on_delete=models.CASCADE, verbose_name=_('image'))
    title = models.CharField(max_length=120, verbose_name=_('title'))

    class Meta:
        verbose_name = _('What we repair')
        verbose_name_plural = _('What we repair')

    def __str__(self):
        return self.title


class Faults(models.Model):
    image = models.ForeignKey(Media, on_delete=models.CASCADE, verbose_name=_('image'))
    title = models.CharField(max_length=120, verbose_name=_('title'))

    class Meta:
        verbose_name = _('Fault')
        verbose_name_plural = _('Faults')

    def __str__(self):
        return self.title


class DescribeFault(models.Model):
    name = models.CharField(max_length=120, verbose_name=_('name'))
    device_type = models.CharField(max_length=120, verbose_name=_('device_type'))
    phone_number = models.CharField(max_length=120, verbose_name=_('phone number'),
                                    validators=[validate_phone_number])
    brand_and_model = models.CharField(max_length=120, verbose_name=_('model'))
    desc = models.TextField(_('description'))
    agree_or_disagree = models.BooleanField(_('agree or disagree'), default=False)

    class Meta:
        verbose_name = _('Describe fault')
        verbose_name_plural = _('Describe faults')

    def __str__(self):
        return self.name


class TypesOfWork(models.Model):
    image = models.ForeignKey(Media, on_delete=models.CASCADE, verbose_name=_('image'))
    title = models.CharField(max_length=120, verbose_name=_('title'))
    problems = RichTextField(_('problems'))

    class Meta:
        verbose_name = _('Types of work')
        verbose_name_plural = _('Types of works')

    def __str__(self):
        return self.title


class WhatWeRepairCategory(MPTTModel):
    image = models.ForeignKey(Media, on_delete=models.SET_NULL,
                              null=True, blank=True, verbose_name=_('image'))
    title = models.CharField(max_length=120, verbose_name=_('title'))
    order = models.IntegerField(_("order"), default=0)
    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            null=True, blank=True,
                            related_name='children')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Service Category")
        verbose_name_plural = _("Service Categories")
        ordering = ['order']

    class MPTTMeta:
        order_insertion_by = ['title']


class Services(models.Model):
    title = models.CharField(max_length=120, verbose_name=_('title'))
    category = models.ForeignKey(WhatWeRepairCategory, on_delete=models.CASCADE,
                                 verbose_name=_('category'), related_name='service_category')
    problems = RichTextField(_('problems'))

    class Meta:
        verbose_name = _('Service')
        verbose_name_plural = _('Services')

    def __str__(self):
        return self.title


class Address(models.Model):
    address = models.CharField(max_length=120, verbose_name=_('address'))
    work_schedule = models.CharField(max_length=120, verbose_name=_('work schedule'))
    phone_number = models.CharField(max_length=120, verbose_name=_('phone number'))
    underground_station = models.CharField(max_length=120, verbose_name=_('underground station'))
    location = models.URLField(_('location'))

    class Meta:
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')