from django.http import HttpResponse


# custom index view method
def index(request):
    return HttpResponse('<h1>Hello, Stranger!</h1> <a href="/picasso/">Picasso</a>')