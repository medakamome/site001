from rest_framework import routers

from .views import DifinitionViewSet


router = routers.DefaultRouter()
router.register(r'difinitions', DifinitionViewSet)