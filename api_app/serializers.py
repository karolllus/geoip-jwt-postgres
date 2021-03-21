from rest_framework import serializers
from api_app.models import GeoModel


class GeoModelSerializer(serializers.Serializer):
    """Geolocation Model Serializer"""
    id = serializers.IntegerField()
    url = serializers.CharField(required=False, allow_blank=True)
    ip = serializers.IPAddressField(required=False)
    type = serializers.CharField(required=False)
    continent_code = serializers.CharField(required=False)
    continent_name = serializers.CharField(required=False)
    country_code = serializers.CharField(required=False)
    country_name = serializers.CharField(required=False)
    region_code = serializers.CharField(required=False)
    region_name = serializers.CharField(required=False)
    city = serializers.CharField(required=False)
    zip = serializers.CharField(required=False)
    latitude = serializers.FloatField(required=False)
    longitude = serializers.FloatField(required=False)


    def create(self, validated_data):
        return GeoModel.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.ip = validated_data.get('ip', instance.ip)
        instance.save()
        return instance