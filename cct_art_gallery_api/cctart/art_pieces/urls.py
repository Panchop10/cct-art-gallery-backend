"""Art Pieces URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import art_pieces as artpieces_views

router = DefaultRouter()
router.register(
    r'art-pieces',
    artpieces_views.ArtPieceViewSet,
    basename='art-pieces'
)
router.register(
    r'art-pieces/(?P<slug_name>[-a-zA-Z0-9_]+)/tags',
    artpieces_views.ArtPieceTagViewSet,
    basename='tags'
)
router.register(
    r'art-pieces/(?P<slug_name>[-a-zA-Z0-9_]+)/details',
    artpieces_views.ArtPieceDetailViewSet,
    basename='details'
)

urlpatterns = [
    path('', include(router.urls))
]
