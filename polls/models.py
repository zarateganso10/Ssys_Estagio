from django.db.models import Model
from django.db.models import CharField


# Create your models here.

class Employee(Model):
	Name = CharField(
		max_length=50, 
		verbose_name='Name',
    	)
	Email = CharField(
		max_length=50, 
		verbose_name='Email',
    	)
	Department = CharField(
		max_length=50,
		verbose_name='Department',
    	)
	



	