# myspacecal.data.admin
# encoding=utf-8

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from models import Agency
from models import Satellite


class AgencyAdmin(admin.ModelAdmin):
    pass
admin.site.register(Agency, AgencyAdmin)

class SatelliteAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Satellite, SatelliteAdmin)
