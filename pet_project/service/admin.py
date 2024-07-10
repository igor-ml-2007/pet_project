from mptt.admin import DraggableMPTTAdmin

from django.contrib import admin

from service.models import *


@admin.register(AboutService)
class AboutServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'advantages']


@admin.register(WhatWeRepair)
class WhatWeRepairAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(Faults)
class FaultsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(DescribeFault)
class DescribeFaultAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'device_type']


@admin.register(TypesOfWork)
class TypesOfWorkAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(WhatWeRepairCategory)
class WhatWeRepairCategoryAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'order', 'title')
    list_display_links = ('title', )


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category']


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['id', 'address']