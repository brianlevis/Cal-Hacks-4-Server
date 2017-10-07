from django.http import JsonResponse


def get_data(request):
    return JsonResponse({'hell yeah?' : 'HELL YEAH!!!'})