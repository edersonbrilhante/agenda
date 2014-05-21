from django.http import HttpResponse
from django.template import RequestContext, loader

from agenda.models import Event

def index(request):
    latest_event_list = Event.objects.order_by('create_date')[:5]
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'latest_event_list': latest_event_list,
    })

    return HttpResponse(template.render(context))

def detail(request, event_id):
    
    template = loader.get_template('event.html')
    event = Event.objects.filter(id = event_id)
    context = RequestContext(request, {
        'event': event[0],
    })
    return HttpResponse(template.render(context))

def fb(request, event_id):
    
    template = loader.get_template('fb.html')
    event = Event.objects.filter(id = event_id)
    context = RequestContext(request, {
        'event': event[0],
    })
    return HttpResponse(template.render(context))

def about(request):
	context = RequestContext(request)
	template = loader.get_template('about.html')
	return HttpResponse(template.render(context))