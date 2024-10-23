from django.db import models

class Students(models.Model):
    rollno = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    branch = models.CharField(max_length=100)
    phone = models.IntegerField()

    def __str__(self):
        return self.name


