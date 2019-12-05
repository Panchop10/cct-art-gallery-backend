"""Artists URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import artists as artist_views

router = DefaultRouter()
router.register(r'artists', artist_views.ArtistViewSet, basename='artist')
# router.register(
#     r'circles/(?P<slug_name>[-a-zA-Z0-9_]+)/members',
#     membership_views.MembershipViewSet,
#     basename='membership'
# )

urlpatterns = [
    path('', include(router.urls))
]
