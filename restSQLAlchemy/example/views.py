from django.shortcuts import render
from example.serializers import PartItemSerializer, CarSerializer
from example.models import Car, PartItem, session
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets



class CarViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = session.query(Car).all()
    serializer_class = CarSerializer
    
# class CarList(APIView):
#     def get(self, request, format=None):
#         cars = session.query(Car).all()
#         serializer = CarSerializer(cars, many= True)
#         return Response(serializer.data)
    
#     def post(self, request, format=None):
#         serializer = CarSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class PartItemList(APIView):
#     def get(self, request, format=None):
#         part_items = session.query(PartItem).all()
#         serializer = PartItemSerializer(part_items, many= True)
#         return Response(serializer.data)
    
