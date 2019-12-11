"""Orders URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import orders as orders_views

router = DefaultRouter()
router.register(r'orders', orders_views.OrderViewSet, basename='order')

urlpatterns = [
    path('', include(router.urls))
]
