
"""items Api view"""
from django.shortcuts import render
from django.http import JsonResponse
from products.models import items
from rest_framework.decorators import api_view
from rest_framework.response import Response


#  create your views here.
from .models import items
from products.serializers import itemsSerializer

# list all items
@api_view(['GET'])
def itemsList(request):
    item = items.objects.all()
    serializer = itemsSerializer(item, many=True)
    return Response(serializer.data)

# bring items by id
@api_view(['GET'])
def itemsDetail(request, pk):
    item = items.objects.get(id=pk)
    serializer = itemsSerializer(item, many=False)
    return Response(serializer.data)

# create items
@api_view(['POST'])
def itemsCreate(request):
    serializer = itemsSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

# update items 
@api_view(['POST'])
def itemsUpdate(request, pk):
    item = items.objects.get(id=pk)
    serializer = itemsSerializer(instance=item, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

# delete items 
@api_view(['DELETE'])
def itemsDelete(request, pk):
    item = items.objects.get(id=pk)
    items.delete()

    return Response('items succsesfully delete!')