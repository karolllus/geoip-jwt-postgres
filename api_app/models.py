from django.contrib.gis.db import models
from django.contrib.postgres.operations import CreateExtension
from django.db import migrations


class Migration(migrations.Migration):
    """ Craete extension postigs"""

    operations = [
        CreateExtension('postgis'),
        ...
    ]


class GeoModel(models.Model):
    """ Database model for Geolocalization"""
    url = models.CharField(null=True, blank=True, default='', max_length=255)
    ip = models.GenericIPAddressField(null=True, blank=True, default='')
    type = models.CharField(null=True, blank=True, max_length=4, default='')
    continent_code = models.CharField(null=True, blank=True, max_length=4, default='')
    continent_name = models.CharField(null=True, blank=True, max_length=255, default='')
    country_code = models.CharField(null=True, blank=True, max_length=4, default='')
    country_name = models.CharField(null=True, blank=True, max_length=255, default='')
    region_code = models.CharField(null=True, blank=True, max_length=4, default='')
    region_name = models.CharField(null=True, blank=True, max_length=255, default='')
    city = models.CharField(null=True, blank=True, max_length=255, default='')
    zip = models.CharField(null=True, blank=True, max_length=255, default='')
    latitude = models.FloatField(null=True, blank=True, default=0.0)
    longitude = models.FloatField(null=True, blank=True, default=0.0)


    def __str__(self):
        return self.ip