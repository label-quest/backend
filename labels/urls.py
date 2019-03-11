from django.urls import path, include
from . import views
from rest_framework import routers
from django.conf.urls import url


router = routers.DefaultRouter()
router.register('labels', views.LabelView)
router.register('label_placement', views.LabelPlacementView, basename='label_placement')


urlpatterns = [
    path('', include(router.urls)),
    url(r'label_placement', views.LabelPlacementView.create_label_placement)
]
