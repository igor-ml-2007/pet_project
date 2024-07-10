from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey
from common.models import Media
from config.settings import AUTH_USER_MODEL
from ckeditor.fields import RichTextField


class ProductCategory(MPTTModel):
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
        verbose_name = _("Product Category")
        verbose_name_plural = _("Product Categories")
        ordering = ['order']

    class MPTTMeta:
        order_insertion_by = ['title']


class Product(models.Model):
    seller = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE,
                               verbose_name=_('seller'))
    title = models.CharField(max_length=120, verbose_name=_('title'))
    image = models.ManyToManyField('MediaLibrary', verbose_name=_('image'))
    price = models.IntegerField(_('price'), default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE,
                                 verbose_name=_('category'))
    location = models.URLField(_('location'))
    desc = models.TextField(_('description'))
    characteristic = RichTextField(_('characteristic'))

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return self.title


class MediaLibrary(models.Model):
    seller = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE,
                               verbose_name=_('seller'))
    image = models.ImageField(upload_to='user_library/')

    class Meta:
        verbose_name = _('MediaLibrary')
        verbose_name_plural = _('MediaLibraries')

    def __str__(self):
        return self.seller.name


class Auction(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('user'))
    suggest_price = models.IntegerField(_('suggest price'), default=0)

    class Meta:
        verbose_name = _('Auction')
        verbose_name_plural = _('Auction')

    def __str__(self):
        return self.user.username


















