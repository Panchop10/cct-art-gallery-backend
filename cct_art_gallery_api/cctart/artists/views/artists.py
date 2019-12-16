"""Artists views."""

# Django REST Framework
from rest_framework import viewsets, mixins, status
from rest_framework.response import Response

# Serializers
from cctart.artists.serializers import ArtistModelSerializer

# Models
from cctart.artists.models import Artist

# Permissions
from cctart.users.permissions import IsAdmin

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
)

# Utilities
import json

class ArtistViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    """Artist view set."""

    serializer_class = ArtistModelSerializer
    lookup_field = 'slug_name'

    def get_permissions(self):
        """Assign permissions based on action."""
        if self.action in ['list', 'retrieve']:
            permissions = [AllowAny]
        elif self.action in ['destroy']:
            permissions = [IsAuthenticated]
        else:
            permissions = [IsAuthenticated]
        return [p() for p in permissions]

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

    def create(self, request, *args, **kwargs):
        """Handle artists creation."""
        serializer = ArtistModelSerializer(
            data=json.loads(request.data['data']),
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        artist = serializer.save()

        data = self.get_serializer(artist).data
        return Response(data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        """Handle update artists"""
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = ArtistModelSerializer(
            instance,
            data=json.loads(request.data['data']),
            partial=partial
        )
        serializer.is_valid(raise_exception=True)
        artist = serializer.save()

        data = self.get_serializer(artist).data
        return Response(data, status=status.HTTP_200_OK)
