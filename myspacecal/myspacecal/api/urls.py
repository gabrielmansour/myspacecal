# myspacecal.api.urls
# encoding=utf-8

from django.conf.urls import patterns, include, url
from myspacecal.api.handlers import AgencyHandler
from myspacecal.api.handlers import ObservationHandler
from myspacecal.api.handlers import RootHandler
from myspacecal.api.handlers import SatelliteHandler
from myspacecal.api.handlers import TargetHandler
from piston.resource import Resource

# This is a public API; no authentication.
#auth = HttpBasicAuthentication(realm="My Realm")
#ad = { 'authentication': auth }
ad = {}

# Resources
root = Resource(handler = RootHandler, **ad)
agencies = Resource(handler = AgencyHandler, **ad)
satellites = Resource(handler = SatelliteHandler, **ad)
targets = Resource(handler = TargetHandler, **ad)
observations = Resource(handler = ObservationHandler, **ad)


urlpatterns = patterns(
    '',
    # satellites
    url(r'^satellites/$', satellites, name='satellites'),
    url(r'^satellites/(?P<slug>.+)$', satellites, name='satellite-detail'),
    # agencies
    url(r'^agencies/$', agencies, name='agencies'),
    url(r'^agencies/(?P<slug>.+)$', agencies, name='agency-detail'),
    # targets
    url(r'^targets/$', targets, name='targets'),
    url(r'^targets/(?P<id>\d+)$', targets, name='target-detail'),
    # observations
    url(r'^observations/$', observations, name='observations'),
    url(r'^observations/(?P<id>\d+)$', observations, name='observation-detail'),
    # root
    url(r'^$', root),
)
