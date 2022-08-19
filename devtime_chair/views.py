from django.shortcuts import render

from .models import Record

from .serializers import RecordSerializer

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class AllRecordsView(APIView):

    def get(self, request):
        records = Record.objects.all().order_by('date')
        serializer = RecordSerializer(records, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class RecordView(APIView):

    def post(self, request):
        data = request.data
        
        serializer = RecordSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)