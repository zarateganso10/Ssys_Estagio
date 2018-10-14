
#importacoes
from rest_framework import serializers
from polls.models import Employee



class EmployeeSerializer(serializers.HyperlinkedModelSerializer): 
	class Meta:
		model = Employee
		fields = ('url','Name','Email','Department')