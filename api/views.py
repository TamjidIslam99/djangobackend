from django.shortcuts import render
from .serializers import StudnetSerializers
from rest_framework.generics import ListAPIView
from .models import Student1
# Create your views here.
class StudentList(ListAPIView):
    queryset=Student1.objects.all()
    serializer_class=StudnetSerializers