from django.contrib import admin
from api.models import PriceGroup, PriceSubGroup, PriceItem


admin.site.register(PriceSubGroup)
admin.site.register(PriceGroup)


@admin.register(PriceItem)
class PriceItemAdmin(admin.ModelAdmin):
    list_filter = ('group', 'sub_group')
    pass