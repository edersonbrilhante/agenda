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
    return HttpResponse("You're looking at event %s." % event_id)
