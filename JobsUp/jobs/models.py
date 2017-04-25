from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
	first_name = models.CharField(max_length = 200, null = True)
	last_name = models.CharField(max_length = 200, null = True)
	email = models.CharField(max_Length = 200, null = False)
	password = models.CharField(max_Length = 200, null = False)
	company_name = models.CharField(max_Length = 200, null = True)
	area_of_interest = models.CharField(max_Length = 200, null = True)
	hashid = models.CharField(max_Length = 50, null = False)