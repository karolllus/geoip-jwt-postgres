# Generated by Django 3.1.7 on 2021-03-21 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0008_auto_20210321_0140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geomodel',
            name='url',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]