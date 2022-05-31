from django.urls import path

# local imports
from picasso import views

app_name = 'picasso'  # app namespace
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('search/', views.search_results, name='search_results'),
    path('category/<str:category>/', views.get_by_category, name='get_by_category'),
]
