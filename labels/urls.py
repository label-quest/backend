from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('labels', views.LabelView)

urlpatterns = [
    path('', include(router.urls))
]
