from django.db import models
from django.contrib.gis.db import models
class Waypoint(models.Model):
    name = models.CharField(max_length=32)
    geometry = models.PointField(srid=4326)
    objects = models.GeoManager()

    def __unicode__(self):
        return '%s %s %s' % (self.name, self.geometry.x, self.geometry.y)
# Create your models here.

REPORT_CATEGORIES = (
    ('1', 'corpse'),
    ('2', 'injured'),
    ('3', 'haven'),
    ('3', 'firstaid'),
)

class Report(models.Model):
    reportCategory = models.CharField(max_length=1, choices=REPORT_CATEGORIES, blank=True)
    reportDetails = models.CharField(max_length=32, blank=True)
    geom = models.PointField(srid=4326, blank=True)
    reportDate = models.DateTimeField(auto_now_add=True, blank=True)
    objects = models.GeoManager()

    def __unicode__(self):
        return '%s %s %s %s %s' % (self.reportCategory, self.geom.x, self.geom.y, self.reportDate, self.reportDetails)
