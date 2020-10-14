from django.db import models
from django.utils import timezone
from movies.models import Movie
class Reviews(models.Model):
    like_choice = ((True, 'Like'), (False, 'Dislike'))
    like_type = models.BooleanField(choices=like_choice)
    up_vote = models.IntegerField(default=0)
    down_vote = models.IntegerField(default=0)
    review = models.CharField(max_length=280)
    date_created = models.DateTimeField(default=timezone.now)
    # movie_actors = models.ForeignKey(Movie, on_delete=models.CASCADE, default=True) 

    @property
    def num_votes(self):
        return self.up_vote - self.down_vote