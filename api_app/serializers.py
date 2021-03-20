from rest_framework import serializers
from api_app.models import GeoModel


class GeoModelSerializer(serializers.Serializer):
    """Geolocation Model Serializer"""
    id = serializers.IntegerField()
    ip = serializers.IPAddressField()


    def create(self, validated_data):
        return GeoModel.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.ip = validated_data.get('ip', instance.ip)
        instance.save()
        return instance