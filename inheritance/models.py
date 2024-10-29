from django.db import models

# Create your models here.
class Abstractmodel(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)

    class Meta:
        abstract = True
#This will inherit properties from parent class but parent class will not be created in db        
class Abstractbaseclass(Abstractmodel):
    phone = models.IntegerField()



# Multy tabel model inheritance
class Multitabel(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class Multibaseclass(Multitabel):
    age = models.IntegerField()   


#Proxy Inheritance
class Proxyinheritance(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username
# cannot add new attributes, but we can get properties from parent
class ProxyBaseclass(Proxyinheritance):
    class Meta:
        proxy = True
        ordering = ['username']    

    def __str__(self):
        return self.username    
