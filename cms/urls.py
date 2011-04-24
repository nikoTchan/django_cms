from django.conf.urls.defaults import *
from cms import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
import os.path

urlpatterns = patterns('',
    # Example:
    # (r'^cms/', include('cms.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
		
    (r'^tiny_mce/(?P<path>.*)$', 'django.views.static.serve',
		  {'document_root': os.path.abspath(os.path.join(settings.STATIC_DIR, 'js/tiny_mce')).replace('\\','/')}),
    (r'^search/$', 'cms.search.views.search'),
    (r'^weblog/$', 'coltrane.views.entries_index'),
    (r'^weblog/(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', 'coltrane.views.entry_detail'),
    (r'', include('django.contrib.flatpages.urls')),
)
