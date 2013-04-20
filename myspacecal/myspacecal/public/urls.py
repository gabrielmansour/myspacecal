# myspacecal.public.urls
# encoding=utf-8

from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'myspacecal.public.views',

    url(r'^$', 'home', name='home'),
    url(r'^about/$', 'about', name='about'),
    url(r'^contact/$', 'contact', name='contact'),
    url(r'^help/$', 'help', name='help'),

    url(r'^agency/(?P<slug>.+)$', 'agency', name='agency-detail'),
    url(r'^satellite/(?P<slug>.+)$', 'satellite', name='satellite-detail'),
)
