"""Categories URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import categories as categories_views

router = DefaultRouter()
router.register(r'categories', categories_views.CategoryViewSet, basename='category')
# router.register(
#     r'circles/(?P<slug_name>[-a-zA-Z0-9_]+)/members',
#     membership_views.MembershipViewSet,
#     basename='membership'
# )

urlpatterns = [
    path('', include(router.urls))
]
