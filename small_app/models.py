from django.db import models

class Emp(models.Model):
    name=models.CharField(max_length=10)
    age=models.IntegerField()
    dept=models.CharField(max_length=10)
    salary=models.IntegerField()
