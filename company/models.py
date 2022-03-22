from django.db import models

'''
kibria Islam 
Jr.Full Stack Developer
kibriaislam82@gmail.com
'''

class Company(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField()
    company = models.ForeignKey(Company, on_delete =  models.CASCADE)


    def __str__(self):
        return self.name


