from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from .models import GeoModel
from .serializers import GeoModelSerializer


# Generic based views

class GenericAPIView(   generics.GenericAPIView, 
                        mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin):
    
    serializer_class = GeoModelSerializer
    queryset = GeoModel.objects.all()

    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)