from django.http import JsonResponse, HttpResponseBadRequest
import subprocess, sys

locations = {}

class Tracker:
    def __init__(self, region_name, lat, lon):
        self.region_name = region_name
        self.lat = lat
        self.lon = lon

def get_data(request):
    print("Get data: " + str(request))
    if request.method != "GET":
        return HttpResponseBadRequest("Request should be a GET request with field region_name.")
    return JsonResponse({'hell yeah?': 'HELL YEAH!!!'})


def add_tracker(request):
    print("Add Tracker: " + str(request))
    if request.method != "GET":
        return HttpResponseBadRequest("Request should be a GET request with fields region_name, latitude, and longitude.")
    try:
        region_name = request.GET['region']
        if region_name in locations:
            HttpResponseBadRequest("Region " + region_name + " already exists.")
        lat, lon = request.GET['latitute'], request.GET['longitude']
        p = subprocess.Popen([sys.executable, 'tracker.py'],
                             stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT)
        locations[region_name] = p
    except KeyError:
        return HttpResponseBadRequest()


def remove_tracker(request):
    print("Remove Tracker: " + str(request))
    if request.method != "GET":
        return HttpResponseBadRequest("Request should be a GET request with fields region_name.")
    try:
        region_name = request.GET['region']
        if region_name in locations:
            HttpResponseBadRequest("Region " + region_name + " already exists.")
        lat, lon = request.GET['latitute'], request.GET['longitude']
        p = subprocess.Popen([sys.executable, 'tracker.py'],
                             stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT)
        locations[region_name] = p
    except KeyError:
        return HttpResponseBadRequest()