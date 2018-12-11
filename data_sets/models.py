import sys
sys.path.append("..")
from django.db import models
from customers.models import Customer


class DataSet(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=4096)
    folder_path = models.CharField(max_length=4096)
    goal = models.FloatField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
