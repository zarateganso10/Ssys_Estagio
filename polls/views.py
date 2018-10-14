from django.shortcuts import render
from django.views.generic import View
from rest_framework import viewsets					
from polls.models import Employee 					#importa a classe employee da pasta models.py
from .serializers import EmployeeSerializer			



# Create your views here.
class EmployeeView(viewsets.ModelViewSet):		
	queryset = Employee.objects.all()
	serializer_class = EmployeeSerializer
