from django.shortcuts import render
from .models import usermodel
from .serializers import dataSerializer
from rest_framework import generics, viewsets


class save_data(generics.ListCreateAPIView):
    queryset = usermodel.objects.all()
    serializer_class = dataSerializer
