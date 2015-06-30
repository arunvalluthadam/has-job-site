from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hasjob_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('app_hasjob.urls')),
    (r'^search/', include('haystack.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
