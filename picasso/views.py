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


def search_results(request):
    categories = Category.objects.all()
    locations = Location.objects.all()

    if 'search_term' in request.GET and request.GET['search_term']:
        search_query = request.GET.get('search_term')
        searched_images = Image.search_image_by_category(
            '', search_query) or Image.filter_image_by_location('', search_query)
        message = f'Results for: {search_query}'
        context = {
            'images': searched_images,
            'categories': categories,
            'title': 'Search Results',
            'message': message
        }
        return render(request, 'picasso/index.html', context)
    else:
        message = 'No results found, Please try again.'
        return render(request, 'picasso/index.html', {'message': message})
