from django import forms
from reviews.models import Reviews


class PostForm(forms.ModelForm):
   class Meta:
       model = Reviews
       fields = ['review', 'like_type']