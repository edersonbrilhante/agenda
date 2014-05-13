from django.conf.urls import patterns, include, url

from django.contrib import admin
from agenda import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'agenda.views.index', name='home'),
    url(r'^(?P<event_id>\d+)/$', views.detail, name='detail'),
    url(r'^events/', include('agenda.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
