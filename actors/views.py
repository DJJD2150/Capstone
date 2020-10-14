from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from actors.models import Actor
from movies.models import Movie

def actor_view(request, actor_id):
    selected_actor = Actor.objects.filter(id=actor_id).first()
    filmography = Movie.objects.filter(actors=selected_actor)    
    return render(request, 'actordetail.html', {'actor': selected_actor, 
                                                'filmography': filmography })