from urllib import response
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import permissions, serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from supplier.models import AddFlightList
from .serializers import AddSerializer


# Create your views here.
class AddViewList1(APIView):
   # permission_classes= [permissions.IsAuthenticated]

   # List all
   def get(self, request, *args, **kwargs):
      listViews= AddFlightList.objects.all()
      serializer= AddSerializer(listViews, many=True)
      return Response({'message': 'success','status':status.HTTP_200_OK})

   # create
   def post(self, request, *args, **kwargs):  
      serializer= AddSerializer(data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response({'message': 'data save','status': status.HTTP_201_CREATED}, status= status.HTTP_201_CREATED)
      return Response({'message': 'Something went wrong', 'status': status.HTTP_400_BAD_REQUEST}, status= status.HTTP_400_BAD_REQUEST )
