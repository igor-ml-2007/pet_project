import datetime
from mptt.models import MPTTModel, TreeForeignKey

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from common.models import Media
from common.utils import validate_phone_number
from config.settings import AUTH_USER_MODEL


class BrandCategory(MPTTModel):
    title = models.CharField(max_length=120, verbose_name=_('title'))
    image = models.ForeignKey(Media, on_delete=models.CASCADE, verbose_name=_('image'))
    order = models.IntegerField(_("order"), default=0)

    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            null=True, blank=True,
                            related_name='children')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Brand Category")
        verbose_name_plural = _("Brand Categories")
        ordering = ['order']

    class MPTTMeta:
        order_insertion_by = ['title']


class ProductImage(models.Model):
    image = models.ForeignKey(Media, on_delete=models.CASCADE, verbose_name=_('image'),
                              related_name='product_image')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name=_('product'),
                                related_name='products')

    class Meta:
        verbose_name = _('Product image')
        verbose_name_plural = _('Product images')

    def __str__(self):
        return self.product.title


class Product(models.Model):
    class Color(models.TextChoices):
        WHITE = 'W'
        BLACK = 'CH'
        BLUE = 'B'
        GREEN = 'G'
        YELLOW = 'Y'
        RED = 'R'
    title = models.CharField(max_length=120, verbose_name=_('title'))
    price = models.IntegerField(_('price'), default=0)
    is_home_page = models.BooleanField(_('is_home_page'), default=False)
    desc = models.TextField(_('description'))
    report = models.ForeignKey('Report', verbose_name=_('report'), on_delete=models.CASCADE)
    category = models.ForeignKey(BrandCategory,
                                 on_delete=models.CASCADE,
                                 verbose_name=_('category'),
                                 related_name='brands')
    color = models.CharField(max_length=120, verbose_name='color',
                             choices=Color.choices, default=Color.WHITE)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return self.title


class Accessories(models.Model):
    title = models.CharField(max_length=120, verbose_name=_('title'))
    price = models.IntegerField(_('price'), default=0)
    image = models.ManyToManyField(Media, verbose_name=_('image'))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_('product'),
                                related_name='accessory')
    desc = models.TextField(_('description'))

    class Meta:
        verbose_name = _('Accessory')
        verbose_name_plural = _('Accessories')

    def __str__(self):
        return self.title


class ProductCharacteristics(models.Model):
    class NumberOfSIM(models.TextChoices):
        ONE = '1', _('one')
        TWO = '2', _('two')
        THREE = '3', _('three')
    diagonal = models.CharField(max_length=120, verbose_name=_('diagonal'))
    operational_memory = models.CharField(max_length=120, verbose_name=_('operational_memory'))
    SIM_quantity = models.CharField(_('quantity sim'), max_length=120,
                                    choices=NumberOfSIM.choices,
                                    default=NumberOfSIM.ONE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_('product'))
    chip = models.CharField(max_length=120, verbose_name=_('chip'))
    built_in_memory = models.CharField(max_length=120, verbose_name=_('built_in_memory'))

    class Meta:
        verbose_name = _('Product Characteristic')
        verbose_name_plural = _('Product Characteristics')

    def __str__(self):
        return self.product.title



class AccessoriesCharacteristics(models.Model):
    material = models.CharField(max_length=120, verbose_name=_("material"))
    accessory = models.ForeignKey(Accessories, on_delete=models.CASCADE, verbose_name=_('accessory'))
    desc = models.TextField(_('description'))

    class Meta:
        verbose_name = _('Accessories Characteristics')
        verbose_name_plural = _('Accessories Characteristics')

    def __str__(self):
        return self.material


class Order(models.Model):
    class OrderPaymentMethod(models.TextChoices):
        BY_CARD = 'by card', _('by card')
        CASH = 'cash', _('cash')

    class Color(models.TextChoices):
        WHITE = 'W'
        BLACK = 'CH'
        BLUE = 'B'
        GREEN = 'G'
        YELLOW = 'Y'
        RED = 'R'

    phone_number = models.CharField(max_length=120, verbose_name=_('phone number'),
                                    validators=[validate_phone_number])
    full_name = models.CharField(_('full name'), max_length=120)
    last_name = models.CharField(_('last_name'), max_length=120)
    quantity = models.IntegerField(_('quantity'), default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_('product'))
    address = models.CharField(_('address'), max_length=120)
    payment_method = models.CharField(_('payment method'), max_length=120,
                                      choices=OrderPaymentMethod.choices,
                                      default=OrderPaymentMethod.CASH)

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    def __str__(self):
        return self.full_name


class Report(models.Model):
    report = models.TextField(_('report'))
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE,
                             verbose_name=_('user'))

    class Meta:
        verbose_name = _('Report')
        verbose_name_plural = _('Report')

    def __str__(self):
        return self.user.username


class OrderItem(models.Model):
    order = models.ForeignKey(Order, verbose_name=_("order"), on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name=_("product"), on_delete=models.CASCADE)
    quantity = models.IntegerField(_("quantity"), default=1)

    class Meta:
        verbose_name = _("order item")
        verbose_name_plural = _("order items")
        unique_together = ("order", "product")

    def __str__(self):
        return f"Id: {self.id}| Q: {self.quantity}"

    @property
    def total_price(self):
        return self.product.price * self.quantity






