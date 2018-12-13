import sys
sys.path.append("..")
from django.db import models
from data_sets.models import DataSet


class PotentialLabel(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=4096)
    data_set = models.ForeignKey(DataSet, related_name='potential_labels', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
