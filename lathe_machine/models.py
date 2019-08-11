from django.db import models

# Create your models here.
class lathe_machine(models.Model):
    lathe=models.CharField(max_length=110)
    uses=models.CharField(max_length=200)
    products_made_by_lathe=models.CharField(max_length=100)
    History=models.CharField(max_length=200)
    types=models.CharField(max_length=100)
    def __str__(self):
        return self.lathe

class Customer(models.Model):
    name=models.CharField(max_length=100)
    product_name=models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Country(models.Model):
    name=models.CharField(max_length=30)
    history=models.TextField()
    president=models.CharField(max_length=22)
    capital=models.CharField(max_length=30)

    def __str__(self):
        return self.name




class Tool(models.Model):
    name = models.CharField(max_length=110)
    uses = models.CharField(max_length=200)
    products_made_by_lathe = models.CharField(max_length=100)
    History = models.TextField()
    types = models.CharField(max_length=100)

    def __str__(self):
        return self.name