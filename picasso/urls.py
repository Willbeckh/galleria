from django.urls import path

# local imports
from picasso.views import index

urlpatterns = [
    path('', index, name='index'),
]
