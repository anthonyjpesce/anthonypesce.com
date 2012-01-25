from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib import admin
from clips import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEVELOPMENT:
    urlpatterns += patterns("django.views",
        url(r"^media/(.*)$", "static.serve", {
            "document_root": settings.MEDIA_ROOT,
            'show_indexes': True, 
            }),
        url(r"^static/(.*)$", "static.serve", {
            "document_root": settings.STATIC_ROOT,
            'show_indexes': True, 
            }),
    )