from django.conf.urls import patterns, include, url

from django.contrib import admin
from agenda import views, settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'agenda.views.index', name='home'),
    url(r'^events/(?P<event_id>\d+)/$', views.detail, name='detail'),
    url(r'^events/', 'agenda.views.index'),
    url(r'^mail/', 'agenda.views.index'),
    url(r'^about/', 'agenda.views.about'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                                    {'document_root': settings.MEDIA_ROOT}),
    )
