from django.shortcuts import render
from rest_framework import viewsets
from todayapp1.serializers import studentdata
from todayapp1.models import student

# Create your views here.


class mystudentdata(viewsets.ModelViewSet):
    queryset = student.objects.all()
    serializer_class = studentdata

    def get_serializes_class(self):
        return mystudentdata
