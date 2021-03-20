from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import GeoModel
from .serializers import GeoModelSerializer


@csrf_exempt
def geomodel_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        ips = GeoModel.objects.all()
        serializer = GeoModelSerializer(ips, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = GeoModelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def geomodel_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        geomodel = GeoModel.objects.get(pk=pk)
    except GeoModel.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = GeoModelSerializer(geomodel)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = GeoModelSerializer(geomodel, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        geomodel.delete()
        return HttpResponse(status=204)