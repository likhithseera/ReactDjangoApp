from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def api_endpoint_one(request):
    data = {"message": "Hola from API endpoint one"}
    return Response(data)

@api_view(['GET'])
def api_endpoint_two(request):
    data = {"message": "Adios from API endpoint two"}
    return Response(data)