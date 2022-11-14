from django.http import HttpResponse


def home(request):
    return HttpResponse("Great! Server run successfully.")