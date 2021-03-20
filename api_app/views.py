from .models import GeoModel
from .serializers import GeoModelSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests

# Class based view API view

URL = 'http://api.ipstack.com/{ip}?access_key=095ec7a9c9a1a21123c10d1119c11bdf'

class geomodel_list(APIView):
    """
    List all ip locations, or create a new ip locations.
    """
    def get(self, request, format=None):
        geomodels = GeoModel.objects.all()
        serializer = GeoModelSerializer(geomodels, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GeoModelSerializer(data=request.data)
        response = requests.get(URL.format(ip=request.data['ip']))
        message = response.json()

        if serializer.is_valid():
            return Response(message)

        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class geomodel_detail(APIView):
    """
    Retrieve, update or delete a ip locations instance.
    """
    def get_object(self, pk):
        try:
            return GeoModel.objects.get(pk=pk)
        except GeoModel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        geomodel = self.get_object(pk)
        serializer = GeoModelSerializer(geomodel)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        geomodel = self.get_object(pk)
        serializer = GeoModelSerializer(geomodel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        geomodel = self.get_object(pk)
        geomodel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)