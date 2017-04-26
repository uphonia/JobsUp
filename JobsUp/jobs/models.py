from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Profile(models.Model):
	#username = models.CharField(max_length = 200, null = True)
	#first_name = models.CharField(max_length = 200, null = True)
	#last_name = models.CharField(max_length = 200, null = True)
	#email = models.EmailField(max_length = 254, null= True)
	#password = models.CharField(max_length = 200, null = True)
	company_name = models.CharField(max_length = 200, null = True)
	area_of_interest = models.CharField(max_length = 200, null = True)
	phone_num = models.CharField(max_length = 200, null = True)
	address = models.CharField(max_length = 200, null = True)
	website = models.CharField(max_length = 200, null = True)
	#personnel = models.CharField(max_length = 200, null = True)
	degree = models.CharField(max_length = 200, null = True)
	resume = models.CharField(max_length = 200, null = True)
	#hashid = models.CharField(max_length = 50, null = True)

class User(models.Model):
	profile = models.OneToOneField(Profile, on_delete = models.CASCADE, primary_key = True,)
	username = models.CharField(max_length = 200, null = True)
	first_name = models.CharField(max_length = 200, null = True)
	last_name = models.CharField(max_length = 200, null = True)
	email = models.EmailField(max_length = 254, null= True)
	password = models.CharField(max_length = 200, null = True)
	#degree = models.CharField(max_length = 200, null = True)
	#phone_num = models.CharField(max_length = 200, null = True)
	hashid = models.CharField(max_length = 50, null = True)

class Company(models.Model):
	profile = models.OneToOneField(Profile, on_delete = models.CASCADE, primary_key = True,)
	username = models.CharField(max_length = 200, null = True)
	first_name = models.CharField(max_length = 200, null = True)
	last_name = models.CharField(max_length = 200, null = True)
	email = models.EmailField(max_length = 254, null= True)
	password = models.CharField(max_length = 200, null = True)
	#company_name = models.CharField(max_length = 200, null = True)
	#website = models.CharField(max_length = 200, null = True)
	#phone_num = models.CharField(max_length = 200, null = True)
	hashid = models.CharField(max_length = 50, null = True)

class Application(models.Model):
	applicant = models.ForeignKey(User)
	company = models.ForeignKey(Company)