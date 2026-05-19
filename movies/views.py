from django.http import HttpResponse
from django.template import loader
from .models import Movie


def index(request):
    Movies = Movie.objects.all()
    template = loader.get_template('index.html')
    
    context = {
        'Movies' : Movie
    }
    return HttpResponse(template.render(context, request))
    
def movie(request, id: int):
    movie = Movie.objects.all(id=id)
    template = loader.get_template('display_movie.html')
    context = {
        'movie' : Movie
    }
    return HttpResponse(template.render(context, request))