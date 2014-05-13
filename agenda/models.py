from django.db import models
from datetime import datetime

class Event(models.Model):
	"""docstring for Events"""
	name = models.CharField(max_length = 50)
	short_description = models.CharField(max_length = 150)
	full_description = models.CharField(max_length = 1500)
	image = models.FileField(upload_to='documents/%Y/%m/%d')
	create_date = models.DateTimeField('Date Published')
	last_alter = models.DateTimeField('last alteratio date')
	last_alter_user = models.CharField(max_length = 50)

