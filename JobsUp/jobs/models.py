from __future__ import unicode_literals

from django.db import models
from geoposition.fields import GeopositionField

# Create your models here.

class Individual(models.Model):
	username = models.CharField(max_length = 200, null = True)
	first_name = models.CharField(max_length = 200, null = True)
	last_name = models.CharField(max_length = 200, null = True)
	email = models.EmailField(max_length = 254, null= True)
	password = models.CharField(max_length = 200, null = True)
	str_address = models.CharField(max_length = 500, null = True)
	city = models.CharField(max_length = 500, null = True)
	state = models.CharField(max_length = 500, null = True)
	zipcode = models.CharField(max_length = 500, null = True)
	phone_num = models.CharField(max_length = 200, null = True)
	degree = models.CharField(max_length = 200, null = True)
	resume = models.CharField(max_length = 200, null = True)
	hashid = models.CharField(primary_key = True, max_length = 50, null = False, default = '0000')

class Company(models.Model):
	username = models.CharField(max_length = 200, null = True)
	first_name = models.CharField(max_length = 200, null = True)
	last_name = models.CharField(max_length = 200, null = True)
	email = models.EmailField(max_length = 254, null= True)
	password = models.CharField(max_length = 200, null = True)
	str_address = models.CharField(max_length = 500, null = True)
	city = models.CharField(max_length = 500, null = True)
	state = models.CharField(max_length = 500, null = True)
	zipcode = models.CharField(max_length = 500, null = True)
	company_name = models.CharField(max_length = 200, null = True)
	website = models.CharField(max_length = 200, null = True)
	phone_num = models.CharField(max_length = 200, null = True)
	hashid = models.CharField(primary_key = True, max_length = 50, null = False, default = '0000')

class Application(models.Model):
	applicant = models.ForeignKey(Individual)
	company = models.ForeignKey(Company)