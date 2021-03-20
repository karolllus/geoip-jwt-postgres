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
    ip = models.GenericIPAddressField(null=False)

    def __str__(self):
        return self.ip