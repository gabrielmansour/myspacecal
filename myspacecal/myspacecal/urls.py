# myspacecal.urls
# encoding=utf-8

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib import admin
from django.contrib.sites.models import Site
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

# Don't need to edit the 'sites' so remove admin interface.
admin.site.unregister(Site)

# public
urlpatterns = patterns(
    '',
    url(r'^api/', include('myspacecal.api.urls', namespace='api', app_name='api')),
    url(r'', include('myspacecal.public.urls', namespace='public', app_name='public')),
)

# admin
urlpatterns += patterns(
    '',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    from os.path import join
    # Serve uploaded "media" files during development.
    media_path = join(settings.MEDIA_URL, "(?P<path>.*)")
    media_path = r"^{}$".format(media_path[1:])
    urlpatterns += patterns(
        '',
        url(media_path, 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
     )
