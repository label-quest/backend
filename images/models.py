import sys
sys.path.append("..")
from django.db import models
from data_sets.models import DataSet


class Image(models.Model):
    file_path = models.CharField(max_length=4096)
    data_set = models.ForeignKey(DataSet, on_delete=models.CASCADE)

    def __str__(self):
        return self.file_path
