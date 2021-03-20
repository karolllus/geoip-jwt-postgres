from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import GeoModel
from .serializers import GeoModelSerializer


# Decorator based views

@api_view(['GET', 'POST'])
def geomodel_list(request):
    """
    List all ip locations, or create a new ip location.
    """
    if request.method == 'GET':
        ips = GeoModel.objects.all()
        serializer = GeoModelSerializer(ips, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = GeoModelSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def geomodel_detail(request, pk):
    """
    Retrieve, update or delete a geomodel
    """
    try:
        geomodel = GeoModel.objects.get(pk=pk)
    except GeoModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GeoModelSerializer(geomodel)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = GeoModelSerializer(geomodel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        geomodel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)