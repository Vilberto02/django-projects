from django.urls import path, include
from rest_framework import routers
from .views import DesignerViewSet, ProgrammerViewSet

router = routers.DefaultRouter()

router.register(r'Programmer', ProgrammerViewSet)
router.register(r'Designer', DesignerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
