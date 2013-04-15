from django.contrib import admin

from hwdefio.hwdef.models import Hardware


class HardwareAdmin(admin.ModelAdmin):
    pass


admin.site.register(Hardware, HardwareAdmin)
