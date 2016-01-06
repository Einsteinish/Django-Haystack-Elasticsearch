from django.conf.urls import patterns, include, url
from django.contrib import admin
from search_app import settings

admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'search_app.views.home', name='home'),
    url(r'^about/', 'search_app.views.about', name='about'),

    url(r'^admin/', include(admin.site.urls)),

    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),

    (r'^search/', include('haystack.urls')),
)
