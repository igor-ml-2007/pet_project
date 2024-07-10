from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _


class Profile(AbstractUser):
    full_name = models.CharField(max_length=120, verbose_name=_('name'))
    last_name = models.CharField(max_length=120, verbose_name=_('surname'))
    profile_avatar = models.ImageField(upload_to='avatars/', null=True, blank=True,
                                       verbose_name=_('avatar'))
    phone_number = models.CharField(max_length=120, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    address = models.TextField(_('address'))
    groups = models.ManyToManyField(Group,
                                    blank=True, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(Permission, blank=True,
                                              related_name='custom_user_permissions')


