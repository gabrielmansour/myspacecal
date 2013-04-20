# myspacecal.data.models
# encoding=utf-8

from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Agency(models.Model):
    """
    """
    # Fields
    name = models.CharField(
        max_length = 100,
        help_text = _("The full agency name")
    )
    acronym = models.CharField(
        max_length = 10,
        help_text = _("The agency acronym")
    )
    slug = models.SlugField(
        max_length = 50,
        help_text = _("URL-friendly name for the agency")
    )
    url = models.URLField(
        help_text = _("Agency home page")
    )

    def get_absolute_url(self):
        return reverse('data:agency-detail', args=[self.slug])

    def link(self):
        return {
            'rel': 'self',
            'url': reverse('api:agency-detail', args=[self.slug]),
        }

    def __unicode__(self):
        return unicode(self.acronym)

    class Meta:
        ordering = ('acronym',)
        verbose_name_plural = _("Agencies")


# CREATE TABLE satellites (
# 	id INT NOT NULL AUTO_INCREMENT,
# 	active INT(1) NOT NULL,
# 	name VARCHAR(256) UNIQUE NOT NULL,
# 	xml_url VARCHAR(512),
# 	classname VARCHAR(256),
# 	color VARCHAR(7) NOT NULL,
# 	last_updated INT NOT NULL,
#     PRIMARY KEY (id)
# ) ENGINE = InnoDB;

class Satellite(models.Model):
    """
    """
    # Fields
    name = models.CharField(
        max_length = 100,
        help_text = _("The name of the satellite")
    )
    slug = models.SlugField(
        max_length = 50,
        help_text = _("URL-friendly name for the satellite")
    )
    agency = models.ManyToManyField(
        Agency,
        related_name = 'satellites',
        help_text = _("Agencies responsbile for the satellite")
    )
    url = models.URLField(
        help_text = _("Satellite home page")
    )
    active = models.BooleanField(
        default = True,
        help_text = _("Is the satellite mission still in-progress?")
    )
    # TODO: make this a custom 'ColorField'.
    color = models.CharField(
        max_length = 7,
        help_text = _("Hex color: #RRGGBB used to represent a satellite")
    )

    def get_absolute_url(self):
        return reverse('data:satellite-detail', args=[self.slug])

    def link(self):
        return {
            'rel': 'self',
            'url': reverse('api:satellite-detail', args=[self.slug]),
        }

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        pass

class InstrumentPackage(models.Model):
    """
    """
    satellite = models.ForeignKey(
        Satellite,
        related_name = "instruments"
    )
    name = models.CharField(
        max_length = 120,
        help_text = _("Human-readable name")
    )
    acronym = models.CharField(
        max_length = 20,
        help_text = _("Acronym")
    )
    description = models.TextField(
        help_text = _("A Markdown-formatted description")
    )
    # WAVELENGTH_UNSPECIFIED = 0
    # WAVELENGTH_XRAY = 1
    # WAVELENGTH_GAMMA_RAY = 2
    # WAVELENGTH_INFRARED = 3
    # WAVELENGTH_MULTI = 4
    # WAVELENGTH = (
    #     (WAVELENGTH_UNSPECIFIED, _("Unspecified")),
    #     (WAVELENGTH_XRAY, _("X-Ray")),
    #     (WAVELENGTH_GAMMA_RAY, _("Gamma Ray")),
    #     (WAVELENGTH_INFRARED, _("Infrared")),
    #     (WAVELENGTH_MULTI, _("Multi-wavelength")),
    # )
    # wavelength = models.PositiveSmallIntegerField(
    #     choices = WAVELENGTH,
    #     default = WAVELENGTH_UNSPECIFIED,
    #     help_text = _("Wavelength that satellite observes")
    # )

    # TODO: add whatever other fields we care about.

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        pass

# CREATE TABLE events (
# 	id INT NOT NULL AUTO_INCREMENT,
# 	id_observation VARCHAR(256) NOT NULL,
# 	id_satellite INT,
# 	start_time DATETIME NOT NULL,
# 	end_time DATETIME NOT NULL,
# 	target VARCHAR(256),
# 	revolution INT,
# 	ra VARCHAR(25),
# 	decl VARCHAR(25),
#     PRIMARY KEY (id),
#     INDEX id_sat (id_satellite),
# 	FOREIGN KEY (id_satellite)
#         REFERENCES satellites(id)
#         ON DELETE CASCADE,
#     UNIQUE (id_observation, id_satellite)
# ) ENGINE = INNODB;

class Target(models.Model):
    """
    """
    # Fields
    name = models.CharField(
        max_length = 100,
        primary_key = True,
        help_text = _("The target name")
    )
    # TODO: create a custom EquatorialCoordField to store this
    # coordinate data.
    # - https://en.wikipedia.org/wiki/Equatorial_coordinate_system
    # - https://en.wikipedia.org/wiki/Sidereal_time
    ra = models.CharField(
        max_length = 24,
        verbose_name = "RA",
        help_text = _("Equatorial coordinates: right ascension")
    )
    dec = models.CharField(
        max_length = 24,
        verbose_name = "Dec",
        help_text = _("Equatorial coordinates: declination")
    )

    def get_absolute_url(self):
        return reverse('data:target-detail', args=[str(self.id)])

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        pass


class Observation(models.Model):
    """
    """
    # Fields
    id = models.PositiveIntegerField(
        max_length = 50,
        primary_key = True,
        help_text = _("Observation ID")
    )
    satellite = models.ForeignKey(
        Satellite,
        related_name = 'observations',
        help_text = _("Satellite performing the observation")
    )
    target = models.ForeignKey(
        Target,
        related_name = 'observations',
        help_text = _("Target being observed")
    )
    revolution = models.PositiveIntegerField(
        help_text = _("Orbital revolution")
    )
    start_time = models.DateTimeField(
        help_text = _("Observation start time")
    )
    finish_time = models.DateTimeField(
        help_text = _("Observation completion time")
    )

    def get_absolute_url(self, request):
        return reverse('data:observation-detail', args=[str(self.id)])

    def __unicode__(self):
        return unicode(self.id)

    class Meta:
        pass
