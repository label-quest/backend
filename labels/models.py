import sys
sys.path.append("..")
from django.db import models
from images.models import Image
from users.models import User


class Label(models.Model):
    x_pos = models.FloatField()
    y_pos = models.FloatField()
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
