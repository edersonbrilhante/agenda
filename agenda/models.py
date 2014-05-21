# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
from django.db.models import signals
from facepy import GraphAPI
from config import USER_TOKEN,PAGE_ID
from settings import MEDIA_ROOT

class Event(models.Model):
	"""docstring for Events"""
	name = models.CharField(max_length = 50)
	short_description = models.CharField(max_length = 150)
	date = models.DateTimeField('date of Event')
	full_description = models.CharField(max_length = 1500)
	image = models.FileField(upload_to = '%Y/%m/%d', null = True, blank = True)
	link = models.URLField(blank = True, null = True)
	create_date = models.DateTimeField('Date Published',auto_now_add=True, editable = False, blank = True, null = True)

	def __str__(self):
		return self.name + ": " + self.short_description

def queue(sender, instance, created, **kwargs):

	name = instance.name
	graph = GraphAPI(USER_TOKEN)

	message = """
Dia %(date)s às %(hour)s o Evento %(name)s
%(short)s

%(long)s

%(link)s
	 """ % {'name': instance.name,
	 		'link': instance.link,
	 		'date': instance.date.strftime('%d/%m/%Y'),
	 		'hour': instance.date.strftime('%H:%M'),
	 		'short': instance.short_description,
	 		'long': instance.full_description,
	 		}
 	

 	if instance.link:
 		graph.post(
	    path = PAGE_ID + '/feed',
	    link = instance.link,
	    message = message)
   
 	else:
		graph.post(
	    path = PAGE_ID + '/photos',
	    source = open( MEDIA_ROOT + "/" + str(instance.image)),
	    message = message)
    






signals.post_save.connect(queue, sender = Event)