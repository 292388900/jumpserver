from django.conf.urls import patterns, include, url
from django.contrib import admin
from jumpserver import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jumpserver.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    (r'^user/', include('juser.urls')),
)
