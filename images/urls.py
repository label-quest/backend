from django.conf.urls import url
from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('images', views.ImageView)
router.register('training_sample', views.TrainingSampleView, basename='training_sample')

urlpatterns = [
    path('', include(router.urls)),
    url(r'training_sample', views.TrainingSampleView.as_view())
]
