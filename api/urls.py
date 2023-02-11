from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import BudgetObjViewSet

router = routers.DefaultRouter()
router.register('budget', BudgetObjViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
