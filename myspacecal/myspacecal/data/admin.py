# myspacecal.data.admin
# encoding=utf-8

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from models import Agency
from models import Satellite
from models import Target
from models import Observation


class AgencyAdmin(admin.ModelAdmin):
    list_display = ('acronym','name',)
admin.site.register(Agency, AgencyAdmin)

class SatelliteAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'wavelength',
        'agencies',
        'operational',
    )
    def agencies(self, obj):
       agency_list = [str(a) for a in obj.agency.all()]
       return ", ".join(agency_list)
    agencies.short_description = _("Agencies")

admin.site.register(Satellite, SatelliteAdmin)

class TargetAdmin(admin.ModelAdmin):
    pass
admin.site.register(Target, TargetAdmin)

class ObservationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Observation, ObservationAdmin)
