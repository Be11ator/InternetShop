from django.contrib import admin

# Register your models here.
from shop.models import *


class CardAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'publish' ,'price', 'brand', 'gender', 'time_create')
    list_display_links = ("id", 'time_create', "title")
    search_fields = ("title", "content",)
    list_editable = ('publish',)
    list_filter = ("publish", "time_create")
    filter_horizontal = ['colors', 'sizes']



admin.site.register(Women, CardAdmin)

class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ("id", )
    search_fields = ('name',)

admin.site.register(Brand, BrandAdmin)

class GenderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', "slug")
    list_display_links = ("id", )
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Gender, GenderAdmin)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ("id", )
    search_fields = ('name',)


admin.site.register(ColorProduct, ColorAdmin)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ("id", )
    search_fields = ('name',)


admin.site.register(SizeProduct, SizeAdmin)