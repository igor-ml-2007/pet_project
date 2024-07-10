from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import *


@admin.register(ProductCategory)
class ProductCategoryAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'order', 'title')
    list_display_links = ('title', )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price']


@admin.register(MediaLibrary)
class MediaLibraryAdmin(admin.ModelAdmin):
    list_display = ['id', 'image']


@admin.register(Auction)
class AuctionAdmin(admin.ModelAdmin):
    list_display = ['id', 'suggest_price']
