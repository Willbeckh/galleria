from django.http import HttpResponse


# custom index view method
def index(request):
    return HttpResponse('Hello, User!')