# myspacecal.data.models
# encoding=utf-8

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
    url = models.URLField(
        help_text = _("Agency home page")
    )

    def __unicode__(self):
        return unicode(self.acronym)

    class Meta:
        ordering = ('acronym',)
        verbose_name_plural = _("Agencies")


class Satellite(models.Model):
    """
    """
    # Fields
    name = models.CharField(
        max_length = 100,
        help_text = _("The name of the satellite")
    )
    agency = models.ManyToManyField(
        Agency,
        related_name = 'satellites',
        help_text = _("Agencies responsbile for the satellite")
    )
    WAVELENGTH_UNSPECIFIED = 0
    WAVELENGTH_XRAY = 1
    WAVELENGTH_GAMMA_RAY = 2
    WAVELENGTH_INFRARED = 3
    WAVELENGTH_MULTI = 4
    WAVELENGTH = (
        (WAVELENGTH_UNSPECIFIED, _("Unspecified")),
        (WAVELENGTH_XRAY, _("X-Ray")),
        (WAVELENGTH_GAMMA_RAY, _("Gamma Ray")),
        (WAVELENGTH_INFRARED, _("Infrared")),
        (WAVELENGTH_MULTI, _("Multi-wavelength")),
    )
    wavelength = models.PositiveSmallIntegerField(
        choices = WAVELENGTH,
        default = WAVELENGTH_UNSPECIFIED,
        help_text = _("Wavelength that satellite observes")
    )
    url = models.URLField(
        help_text = _("Satellite home page")
    )
    operational = models.BooleanField(
        default = True,
        help_text = _("Is the satellite mission still in-progress?")
    )

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        pass


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
