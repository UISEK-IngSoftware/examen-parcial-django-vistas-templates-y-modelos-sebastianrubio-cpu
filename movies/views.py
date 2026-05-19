from django.shortcuts import render, get_object_or_404
from .models import Movie

def index(request):
    # Obtiene todas las películas
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'index.html', context)
    
def movie(request, id):
    # Error 404 me lo dio el visual 
    movie_obj = get_object_or_404(Movie, id=id)
    context = {
        'movie': movie_obj
    }
    return render(request, 'display_movie.html', context)