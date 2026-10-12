from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serialayzer import *

@api_view(['GET'])
def get_products(request):
    products = Product.objects.all()
    serializer = ProductSerialayzer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_one_product(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({'error': 'Not found'}, status=404)

    serializer = ProductSerialayzer(product)
    return Response(serializer.data)


@api_view(['POST'])
def create_product(request):
    serializer = ProductSerialayzer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['PUT'])
def update_product(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({'error': 'Not found'}, status=404)

    serializer = ProductSerialayzer(product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def delete_product(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({'error': 'Not found'}, status=404)

    product.delete()
    return Response(status=204)