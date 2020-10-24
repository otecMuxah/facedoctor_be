from django.urls import path, include
from rest_framework import routers

from api.views import PriceItemViewSet

router = routers.DefaultRouter()
router.register('price', PriceItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
