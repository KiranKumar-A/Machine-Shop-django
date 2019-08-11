from django.db import models

# Create your models here.
class lathe_machine(models.Model):
    lathe=models.CharField(max_length=110)
    uses=models.CharField(max_length=200)
    products_made_by_lathe=models.CharField(max_length=100)
    History=models.CharField(max_length=200)
    types=models.CharField(max_length=100)
    def __str__(self):
        return self.lathe,self.uses,self.products_made_by_lathe,self.History,self.types


