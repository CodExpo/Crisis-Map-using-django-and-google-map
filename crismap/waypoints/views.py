from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from pip._vendor import requests
from django.template.response import TemplateResponse
from django.template.loader import render_to_string
from crismap.waypoints.models import Waypoint, Report
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from datetime import datetime
from Crypto.Random.random import randint
from djgeojson.views import GeoJSONLayerView
import simplejson

#===============================================================================
# def index(requests):
#     'Display Map'
#     return render_to_response('waypoints/index.html',{
#
#                                                       })
#===============================================================================
@csrf_protect
def index(request):
    'Display map'
    waypoints = Waypoint.objects.order_by('name')
    reports = Report.objects.order_by('id')
    cntx = {
        'reports': reports,
        'waypoints': waypoints,
    }
    cntx.update(csrf(request))
    return render(request, "waypoints/index.html",cntx )

@csrf_protect
def save(request):
    'Save waypoints'
    for waypointString in request.POST.get('waypointsPayload', '').splitlines():
        waypointID, waypointX, waypointY = waypointString.split()
        waypoint = Waypoint.objects.get(id=int(waypointID))
        waypoint.geometry.set_x(float(waypointX))
        waypoint.geometry.set_y(float(waypointY))
        waypoint.save()
    for reportString in request.POST.get('reportPayload', '').splitlines():
        reportCat, reportX, reportY  = reportString.split()
        reportDet = request.POST.get('detailsAdded', '')
        if reportDet == "test-val":
            for x in range(0, 30):
                down = 35.6645 + randint(0,1100) * 0.0001
                left = 51.2292 + randint(0,3600) * 0.0001
                tp = 'POINT(' + str(left) + ' ' + str(down) + ')'
                Report(reportCategory='2', reportDetails='test value', geom=tp).save()
            for x in range(0, 10):
                down = 35.6645 + randint(0,1100) * 0.0001
                left = 51.2292 + randint(0,3600) * 0.0001
                tp = 'POINT(' + str(left) + ' ' + str(down) + ')'
                Report(reportCategory='1', reportDetails='test value', geom=tp).save()
            for x in range(0, 10):
                down = 35.6645 + randint(0,1100) * 0.0001
                left = 51.2292 + randint(0,3600) * 0.0001
                tp = 'POINT(' + str(left) + ' ' + str(down) + ')'

            for x in range(0, 10):
                down = 35.6645 + randint(0,1100) * 0.0001
                left = 51.2292 + randint(0,3600) * 0.0001
                tp = 'POINT(' + str(left) + ' ' + str(down) + ')'
                Report(reportCategory='4', reportDetails='test value', geom=tp).save()
        rg = 'POINT(' + str(reportX) + ' ' + str(reportY) + ')'
        Report(reportCategory=reportCat, reportDetails=reportDet, geom=rg).save()
    return HttpResponse(simplejson.dumps(dict(isOk=1)), mimetype='application/json')


def send_file(request):
    from django.core.servers.basehttp import FileWrapper
    from django.contrib.gis.geos import GEOSGeometry
    import mimetypes

    handle = open('exp.kml','w+')
    handle.write('<?xml version="1.0" encoding="UTF-8"?><kml xmlns="http://www.opengis.net/kml/2.2"><Document><name>MynameKML file polygon </name><description>Some descrition</description><Folder>')
    pnts = Report.objects.all()
    for pnt in pnts:
        pnt2 = GEOSGeometry(pnt.geom)
        handle.write(pnt2.kml)
    handle.write('</Folder></Document></kml>')
    handle.close()
    filename = "exp.kml" # Select your file here.
    download_name ="exp.kml"
    wrapper = FileWrapper(open(filename))
    content_type = mimetypes.guess_type(filename)[0]
    response = HttpResponse(wrapper,content_type=content_type)
    response['Content-Length'] = os.path.getsize(filename)
    response['Content-Disposition'] = "attachment; filename=%s"%download_name
    return response

class ReportLayer(GeoJSONLayerView):
    def get_queryset(self):
        context = Report.objects.filter(reportCategory=self.args[0])
        return context


@csrf_exempt
def jsave(request):
    import simplejson as json
    data = json.loads(request.body)
    left, right, non = data['geo'].split(',')
    left = int(left)
    right = int(right)
    tp = 'POINT(' + str(right*0.000001) + ' ' + str(left*0.000001) + ')'
    Report(reportCategory=data['cat'], reportDetails=data['des'], geom=tp).save()

