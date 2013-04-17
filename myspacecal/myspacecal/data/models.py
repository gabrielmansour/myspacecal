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
        help_text = _("The agency name")
    )
    url = models.URLField(
        help_text = _("Agency home page")
    )

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
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
        help_text = _("Agencies responsbile for the satellite")
    )
    url = models.URLField(
        help_text = _("Satellite home page")
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
    right_ascension = models.FloatField(
        help_text = _("Right ascension, radians")
    )
    declinaton = models.TimeField(
        help_text = _("Declination, radians")
    )

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        pass


class Observation(models.Model):
    """
    """
    # Fields
    satellite = models.ForeignKey(
        Satellite,
        help_text = _("Satellite performing the observation")
    )
    target = models.ForeignKey(
        Target,
        help_text = _("Target being observed")
    )
    name = models.CharField(
        max_length = 50,
        help_text = _("")
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
