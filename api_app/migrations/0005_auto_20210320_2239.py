# Generated by Django 3.1.7 on 2021-03-20 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0004_auto_20210320_2137'),
    ]

    operations = [
        migrations.AddField(
            model_name='geomodel',
            name='city',
            field=models.CharField(default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='geomodel',
            name='continent_code',
            field=models.CharField(default='', max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='geomodel',
            name='continent_name',
            field=models.CharField(default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='geomodel',
            name='country_code',
            field=models.CharField(default='', max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='geomodel',
            name='country_name',
            field=models.CharField(default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='geomodel',
            name='latitude',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='geomodel',
            name='longitude',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='geomodel',
            name='region_code',
            field=models.CharField(default='', max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='geomodel',
            name='region_name',
            field=models.CharField(default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='geomodel',
            name='zip',
            field=models.CharField(default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='geomodel',
            name='type',
            field=models.CharField(default='', max_length=4, null=True),
        ),
    ]
