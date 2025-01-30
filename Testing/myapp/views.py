from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import SalesOrderSerializer

def home_view(request):
    return render(request, 'myapp/home.html')



@api_view(['POST'])
def create_sales_order(request):
    if request.method == 'POST':
        serializer = SalesOrderSerializer(data=request.data)
        
        if serializer.is_valid():
            # Save the data to the database
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
