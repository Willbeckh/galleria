from django.shortcuts import render

# LOCAL IMPORTS
from picasso.models import Image

# Create your views here.
def index(request):
    images = Image.objects.all()
    context = {
        'images': images,
        'title': 'Home'
    }
    return render(request, 'picasso/index.html', context)