from django.conf.urls import *
from djgeojson.views import GeoJSONLayerView
from crismap.waypoints.models import Waypoint, Report
from crismap.waypoints import views

urlpatterns = patterns('crismap.waypoints.views',
                       url(r'^$','index',name='waypoints_index'),
                       url(r'^save$', 'save', name='waypoints_save'),
                       url(r'^exp.kml$', 'send_file'),
                       url(r'^data.geojson$', GeoJSONLayerView.as_view(model=Report), name='data'),
                       url(r'^([\w-]+)/data.geojson$', views.ReportLayer.as_view(model=Report)),
                       url(r'^jsave/$', views.jsave ),
                       )