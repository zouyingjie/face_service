from django.conf.urls import patterns, include, url

from django.contrib import admin

from face.views import FaceValidApiView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^api/v2/face-valid/', FaceValidApiView.as_view(), name="api_v2_face_valid_view")
)
