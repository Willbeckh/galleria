from django.urls import path

# local imports
from picasso import views

app_name = 'picasso'  # app namespace
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('search/', views.search_results, name='search_results'),
]
