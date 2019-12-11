"""Users URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import users as users_views

router = DefaultRouter()
router.register(r'users', users_views.UserViewSet, basename='user')
router.register(
    r'users/(?P<username>[-a-zA-Z0-9_]+)/likes',
    users_views.UserLikesViewSet,
    basename='likes'
)
router.register(
    r'users/(?P<username>[-a-zA-Z0-9_]+)/orders',
    users_views.UserOrderViewSet,
    basename='orders'
)

urlpatterns = [
    path('', include(router.urls))
]
