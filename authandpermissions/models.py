from django.db import models

# Create your models here.

class Authoriseuser(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    notes = models.TextField()

    def __str__(self):
        return self.name
