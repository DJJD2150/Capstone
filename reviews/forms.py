from django import forms
from reviews.models import Reviews
from movies.models import Movie

class PostForm(forms.ModelForm):
   class Meta:
       model = Reviews
       fields = ['review', 'like_type']