from django.db import models
from datetime import datetime

class Event(models.Model):
	"""docstring for Events"""
	name = models.CharField(max_length = 50)
	short_description = models.CharField(max_length = 150)
	date = models.DateTimeField('date of Event')
	full_description = models.CharField(max_length = 1500)
	image = models.FileField(upload_to = '%Y/%m/%d')
	link = models.URLField(blank = True, null = True)
	create_date = models.DateTimeField('Date Published',auto_now_add=True, editable = False, blank = True, null = True)

