from django.shortcuts import render

# LOCAL IMPORTS
from picasso.models import Image, Category, Location

# Create your views here.
def index(request):
    images = Image.objects.order_by('-pub_date')[:5]
    categories = Category.objects.all()
    location = Location.objects.all()
    context = {
        'images': images,
        'categories': categories,
        'location': location,
        'title': 'Home'
    }
    return render(request, 'picasso/index.html', context)


def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'picasso/about.html', context)
