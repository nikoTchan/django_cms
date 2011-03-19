from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^django_cms/', include('django_cms.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
		
    (r'^tiny_mce/(?P<path>.*)$', 'django.views.static.serve',
								 {'document_root': '/Users/marc/Sites/django_cms/jscripts/tiny_mce/'}),
    (r'^search/$', 'django_cms.search.views.search'),
    (r'', include('django.contrib.flatpages.urls')),
)
