from django.db import models

# Create your models here.
class Jokes(models.Model):
    question = models.CharField(max_length=100,blank=False) #max_length = required
    response = models.CharField(max_length=200,blank=False)
    
def __str__(self):
    return self.response
