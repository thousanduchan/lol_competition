from django.db import models
from django.utils import timezone




class Team(models.Model):
    name = models.CharField(max_length=20)
    members = models.TextField(max_length=1000)
    score = models.IntegerField()
    image = models.ImageField(upload_to='images/team', null=True)

    def __str__(self):
        return self.name
