"""Artists views."""

# Django REST Framework
from rest_framework import viewsets, mixins

# Serializers
from cctart.artists.serializers import ArtistModelSerializer

# Models
from cctart.artists.models import Artist

class ArtistViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    """Artist view set."""

    serializer_class = ArtistModelSerializer
    lookup_field = 'slug_name'

    def get_queryset(self):
        """Restrict list to active-only."""

        queryset = Artist.objects.all()
        if self.action == 'list':
            return queryset.filter(is_active=True)
        return queryset

    def perform_destroy(self, instance):
        """Disable artist."""
        instance.is_active = False
        instance.save()
