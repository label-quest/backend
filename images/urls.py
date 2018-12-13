from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('images', views.ImageView)
router.register('training_sample', views.TrainingSample)

urlpatterns = [
    path('', include(router.urls))
]
