from django.db import models

class Owner(models.Model):
    name = models.CharField(max_length=128)
    contact = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    contact = models.IntegerField()
    address = models.CharField(max_length=128)
    owner = models.ForeignKey(Owner,on_delete=models.CASCADE)
    employee_size = models.IntegerField()