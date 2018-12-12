import sys
sys.path.append("..")
from .views import CustomerView
from data_sets.views import DataSetView
from django.urls import path, include
from rest_framework_extensions.routers import NestedRouterMixin
from rest_framework import routers


class NestedDefaultRouter(NestedRouterMixin, routers.DefaultRouter):
    pass


router = NestedDefaultRouter()
customers_router = router.register('customers', CustomerView)
customers_router.register(
    'data_sets', DataSetView,
    base_name='customer-data_sets',
    parents_query_lookups=['customer'])

urlpatterns = [
    path('', include(router.urls))
]
