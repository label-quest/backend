import sys
sys.path.append("..")
from django.db import models
from customers.models import Customer
from potential_labels.models import PotentialLabel


class DataSet(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=4096)
    folder_path = models.CharField(max_length=4096)
    goal = models.FloatField()
    customer = models.ForeignKey('customers.Customer', on_delete=models.CASCADE)
    potential_label = models.ForeignKey('potential_labels.PotentialLabel', on_delete=models.CASCADE)
