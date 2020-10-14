from django.db import models
from django.contrib.auth.models import AbstractUser
from reviews.models import Reviews
# Create your models here.
#put date user signed up here for final model 

class BaseUser(AbstractUser):
    name = models.CharField(blank=True, null=True, max_length=25)
    email = models.EmailField(blank=True, null=True)
    homepage = models.URLField(blank=True, null=True)
    display_name = models.CharField(blank=True, null=True, max_length=80)
    follows = models.ManyToManyField("self", symmetrical=False)
    user_pic = models.ImageField(upload_to='images/', null=True, blank=True)
    # review_options = models.ForeignKey(Reviews , on_delete=models.CASCADE, default=True)