from mptt.admin import DraggableMPTTAdmin

from django.contrib import admin

from shop.models import *


@admin.register(BrandCategory)
class BrandCategoryAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'order', 'title')
    list_display_links = ('title', )


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'image']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price']


@admin.register(Accessories)
class AccessoriesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(ProductCharacteristics)
class ProductCharacteristicsAdmin(admin.ModelAdmin):
    list_display = ['id', 'SIM_quantity']


@admin.register(AccessoriesCharacteristics)
class AccessoriesCharacteristicsAdmin(admin.ModelAdmin):
    list_display = ['id', 'desc']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'product']


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']



