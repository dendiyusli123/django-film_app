from django.urls import path
from . import views

app_name = 'film_app'
urlpatterns = [
    path(
        'films',
        views.FilmList.as_view(),
        name = 'MovieList'
    ),
]