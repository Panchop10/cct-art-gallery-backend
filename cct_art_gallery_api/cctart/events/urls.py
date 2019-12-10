"""Events URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import events as events_views

router = DefaultRouter()
router.register(r'events', events_views.EventViewSet, basename='event')
router.register(
    r'events/(?P<slug_name_event>[-a-zA-Z0-9_]+)/artpieces',
    events_views.EventArtPieceViewSet,
    basename='artpieces'
)

urlpatterns = [
    path('', include(router.urls))
]
