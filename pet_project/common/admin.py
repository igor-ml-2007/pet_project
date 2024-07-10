from django.contrib import admin
from common.models import *


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ['id', 'file_type']
    list_filter = ['file_type']


@admin.register(CommonSettings)
class CommonSettingsAdmin(admin.ModelAdmin):
    list_display = ['id', 'our_shop_text']