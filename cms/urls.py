from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
import os.path

ROOT_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__))).replace('\\','/')
STATIC_DIR = os.path.join(ROOT_DIR, 'static').replace('\\','/')

urlpatterns = patterns('',
    # Example:
    # (r'^cms/', include('cms.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
		
    (r'^tiny_mce/(?P<path>.*)$', 'django.views.static.serve',
		  {'document_root': os.path.abspath(os.path.join(STATIC_DIR, 'js/tiny_mce')).replace('\\','/')}),
    (r'^search/$', 'cms.search.views.search'),
    (r'', include('django.contrib.flatpages.urls')),
)
