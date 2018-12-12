import sys
sys.path.append("..")
from django.db import models


class PotentialLabel(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=4096)