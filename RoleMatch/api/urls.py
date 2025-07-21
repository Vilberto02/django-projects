from django.urls import path, include
from rest_framework import routers
from .views import ProgramadorViewSet, DisenadorViewSet

router = routers.DefaultRouter()

router.register(r'Programador', ProgramadorViewSet)
router.register(r'Disenador', DisenadorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
