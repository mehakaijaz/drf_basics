from django.shortcuts import render
from api.serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class ProductsView(APIView):
    def get(self,request):
        queryset = Product.objects.all().order_by("name")
        serializer=ProductSerializer(queryset,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            
class ProductView(APIView): 
    def single_product(self,id_args):
        try:
            queryset = Product.objects.get(id=id_args)
            return queryset
        except Product.DoesNotExist:
            return None
        
    def get(self,request,id_args):
        queryset = self.single_product(id_args)
        if queryset:
            serializer=ProductSerializer(queryset)
            return Response(serializer.data)
        
        else:
            
            return Response({"msg":f"product with the id:{id_args} does not exist"},status=status.HTTP_400_BAD_REQUEST)