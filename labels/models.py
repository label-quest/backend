import sys
sys.path.append("..")
from django.db import models
from images.models import Image
from users.models import User
from potential_labels.models import PotentialLabel


class Label(models.Model):
    x_pos = models.FloatField()
    y_pos = models.FloatField()
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    potential_label = models.ForeignKey(PotentialLabel, on_delete=models.CASCADE)

    def __str__(self):
        return self.potential_label.name + "/" + self.user.username