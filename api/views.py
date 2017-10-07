from django.http import JsonResponse, HttpResponseBadRequest
import subprocess

listeners = {}

LISTENER_SCRIPT = 'listener/listener.py'


def get_events(request):
    print("Get data: " + str(request))
    if request.method != "GET" or ('trackerId' not in request.GET):
        return HttpResponseBadRequest("Request should be a GET request with field trackerId.")
    response = {
        'ClownCon 2017': {
            'name': 'ClownCon 2017',
            'latitude': 37.869407,
            'longitude': -122.266937,
        },
        'Cal Hacks 4.0': {
            'name': 'Cal Hacks 4.0',
            'latitude': 37.870642,
            'longitude': -122.251471,
        },
        'Water Polo Championship': {
            'name': 'Water Polo Championship',
            'latitude': 37.868723,
            'longitude': -122.262037,
        },
    }
    return JsonResponse(response)


def get_tweets(request):
    print("Get event: " + str(request))
    if request.method != "GET" or ('trackerId' not in request.GET) or ('trackerId' not in request.GET):
        return HttpResponseBadRequest("Request should be a GET request with field trackerId.")
    return JsonResponse({'hell yeah?': 'HELL YEAH!!!'})


def add_tracker(request):
    print("Add Tracker: " + str(request))
    if request.method != "GET" or 'id' not in request.GET:
        return HttpResponseBadRequest("Request should be a GET request with fields id, latitude, and longitude.")

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
