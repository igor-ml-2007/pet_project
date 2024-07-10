from django.db import models

from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext_lazy as _


class Media(models.Model):
    class FileType(models.TextChoices):
        IMAGE = 'image', _("Image")
        VIDEO = 'video', _("Video")
        DOCUMENT = 'document', _("document")
        GIF = 'gif', _("Gif")
        OTHER = 'other', _("Other")

    file = models.FileField(upload_to='only_medias/',
                            verbose_name=_("File"),
                            validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'mp4', 'avi',
                                                                                   'mov', 'gif', 'webp', 'pdf', 'doc',
                                                                                   'docx', 'mpeg'])])
    file_type = models.CharField(max_length=10, verbose_name=_("File Type"),
                                 choices=FileType.choices)

    class Meta:
        verbose_name = _("Media")
        verbose_name_plural = _("Media")

    def __str__(self):
        # E:\Azamat Python\1 month\1 lesson\main.py
        element = r"""[\]"""
        return f'Id: {self.id}|Name: {self.file.name.split(element)[-1]}'

    def clean(self):
        if self.file_type not in self.FileType.values:
            raise ValidationError(_("Invalid File Type"))
        elif self.file_type == self.FileType.IMAGE:
            if self.file.name.split('.')[-1] not in ['jpg', 'jpeg', 'png', 'webp']:
                raise ValidationError(_("Invalid Image File"))
        elif self.file_type == self.FileType.VIDEO:
            if self.file.name.split('.')[-1] not in ['mp4', 'avi', 'mov', 'mpeg']:
                raise ValidationError(_("Invalid Video File"))


class CommonSettings(models.Model):
    our_shop_text = models.TextField(verbose_name=_("Our Clinic Text"))
    service_page_back_image = models.ForeignKey(Media,
                                                on_delete=models.CASCADE,
                                                verbose_name=_("Service Page Back Image"),
                                                related_name='service_page_back_image')
    discount_page_back_image = models.ForeignKey(Media,
                                                on_delete=models.CASCADE,
                                                verbose_name=_("Vacancy Page Back Image"),
                                                related_name='vacancy_page_back_image')

    def __str__(self):
        return self.our_shop_text

    class Meta:
        verbose_name = _("Common Settings")
        verbose_name_plural = _("Common Settings")
