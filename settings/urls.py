from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from face.urls import urlpatterns as face_urls
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'FaceIdService.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += face_urls