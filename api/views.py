from django.http import JsonResponse, HttpResponseBadRequest
import subprocess

listeners = {}

LISTENER_SCRIPT = 'listener/listener.py'


def get_tweets(request):
    print("Get event: " + str(request))
    if request.method != "GET" or ('region' not in request.GET) or ('event' not in request.GET):
        return HttpResponseBadRequest("Request should be a GET request with fields region and event.")
    return JsonResponse({'hell yeah?': 'HELL YEAH!!!'})


def get_events(request):
    print("Get data: " + str(request))
    if request.method != "GET" or ('event' not in request.GET):
        return HttpResponseBadRequest("Request should be a GET request with field region.")
    return JsonResponse({'hell yeah?': 'HELL YEAH!!!'})


def add_tracker(request):
    print("Add Tracker: " + str(request))
    if request.method != "GET" or 'region' not in request.GET:
        return HttpResponseBadRequest("Request should be a GET request with fields region, latitude, and longitude.")

    region = request.GET['region']
    if region in listeners:
        HttpResponseBadRequest("Region " + region + " already exists.")

    latitude, longitude = request.GET['latitude'], request.GET['longitude']
    p = subprocess.Popen([LISTENER_SCRIPT, '--region', region, '--latitude', latitude, '--longitude', longitude],
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
    listeners[region] = p


def remove_tracker(request):
    print("Remove Tracker: " + str(request))
    if request.method != "GET":
        return HttpResponseBadRequest("Request should be a GET request with fields region_name.")
    return JsonResponse({'hell yeah?': 'HELL YEAH!!!'})
