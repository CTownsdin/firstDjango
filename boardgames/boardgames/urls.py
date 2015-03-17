from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'boardgames.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # incoming request URLs are mapped to views here.
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'main.views.home')
)
