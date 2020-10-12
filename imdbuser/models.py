from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
#put date user signed up here for final model 

class BaseUser(AbstractUser):
    name = models.CharField(blank=True, null=True, max_length=25)
    email = models.EmailField(blank=True, null=True)
    homepage = models.URLField(blank=True, null=True)
    display_name = models.CharField(blank=True, null=True, max_length=80)
    follows = models.ManyToManyField("self", symmetrical=False)