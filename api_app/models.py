from django.contrib.gis.db import models
from django.contrib.postgres.operations import CreateExtension
from django.db import migrations


class Migration(migrations.Migration):

    operations = [
        CreateExtension('postgis'),
        ...
    ]

class Casino(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    location = models.PointField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name