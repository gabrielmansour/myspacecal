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
        unique = True,
        help_text = _("The target name")
    )

    # These fields are defined as xsd:decimal in the published schema
    # of the existing app. Conforming implementations need to have
    # minimum of 18 significant digits, but no maximum is specified.

    ra = models.DecimalField(
        max_digits = 32,
        decimal_places = 8,
        verbose_name = "RA",
        help_text = _("Right ascension")
    )
    dec = models.DecimalField(
        max_digits = 32,
        decimal_places = 8,
        verbose_name = "DEC",
        help_text = _("Declination")
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
