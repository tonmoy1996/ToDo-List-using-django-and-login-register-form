from django.shortcuts import render
from rest_framework import generics
from  task.models import Task
from api.serializers import TaskSerializer
# Create your views here.

class TaskApiView(generics.ListCreateAPIView):
    
    queryset= Task.objects.all()
    serializer_class= TaskSerializer