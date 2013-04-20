# myspacecal.api.handlers
# encoding=utf-8

from django.core.urlresolvers import reverse
from myspacecal.data.models import Agency
from myspacecal.data.models import Observation
from myspacecal.data.models import Satellite
from myspacecal.data.models import Target
from piston.handler import BaseHandler
from piston.utils import rc, throttle
import re

def make_url(request, url_name, args=None):
    return \
      "http://" + \
      request.META['HTTP_HOST'] + \
      reverse(url_name, args)

## NB: it would be nice if we supported XML, JSON, and CVS as output
## formats. To be properly RESTful we should determine output format
## on the basis of the Accept header.

# class ArbitraryDataHandler(BaseHandler):
#     methods_allowed = ('GET',)
#
#     def read(self, request, username, data):
#         user = User.objects.get(username=username)
#
#         return { 'user': user, 'data_length': len(data) }

class RootHandler(BaseHandler):
    allowed_methods = ('GET',)

    def read(self, request):
        directory =  [
            {'rel': 'agencies',
             'url': make_url(request, 'api:agencies'),},
            {'rel': 'satellites',
             'url': make_url(request, 'api:satellites'),},
            {'rel': 'targets',
             'url': make_url(request, 'api:targets'),},
            {'rel': 'observations',
             'url': make_url(request, 'api:observations'),}]
        return directory

class AgencyHandler(BaseHandler):
    allowed_methods = ('GET',)
    model = Agency
    fields =  ('acronym','name','url','link',('satellites', ()))
    exclude = ('slug',)

    def read(self, request, slug=None):
        if slug:
            # get_object_or_404
            agency = Agency.objects.get(slug=slug)
        else:
            agency = Agency.objects.all()
        return agency

class SatelliteHandler(BaseHandler):
    allowed_methods = ('GET',)
    fields = ('id','name','link','url','active',)
    exclude = ('slug',)
    model = Satellite

    def read(self, request, slug=None):
        if slug:
            satellite = Satellite.objects.get(slug=slug)
        else:
            satellite = Satellite.objects.all()
        return satellite

class TargetHandler(BaseHandler):
    allowed_methods = ('GET',)
    model = Target

    def read(self, request, id=None):
        if id:
            target = Target.objects.get(id=id)
        else:
            target = Target.objects.all()
        return target

class ObservationHandler(BaseHandler):
    allowed_methods = ('GET',)
    model = Observation

    def read(self, request, id=None):
        if id:
            observation = Observation.objects.get(id=id)
        else:
            observation = Observation.objects.all()
        return observation
