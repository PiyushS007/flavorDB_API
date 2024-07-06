from django.shortcuts import render

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from rest_framework.response import Response
from .models import FDB_entities
from .Serializer import FDBEntitiesSerializer
from .services import ServiceLayer

service_layer = ServiceLayer()

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_homepath(request):
    return Response({"message": "Flavordb Entity"})

@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def get_entity(request, id):
    entity = service_layer.get_entity(id)
    serializer = FDBEntitiesSerializer(entity)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def get_entities(request):
    category = request.GET.get('category')
    name = request.GET.get('name')
    entities = service_layer.get_entities(category, name)
    serializer = FDBEntitiesSerializer(entities, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def get_entity_by_natural_source(request, natural_source):
    entities = service_layer.get_entity_by_natural_source(natural_source)
    serializer = FDBEntitiesSerializer(entities, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def entity_autocomplete(request):
    category = request.GET.get('category', '')
    natural_source = request.GET.get('naturalsource', '')
    results = service_layer.search(category,  natural_source)
    #serializer = FDBEntitiesSerializer(results, many=True)
    return Response(results)

