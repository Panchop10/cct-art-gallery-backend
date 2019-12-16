"""Art Pieces views."""

# Django REST Framework
from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

# Serializers
from cctart.art_pieces.serializers import (
    ArtPieceModelSerializer,
    AddArtPieceModelSerializer,
    UpdateArtPieceModelSerializer,
    ArtPieceDetailModelSerializer,
    ArtPieceTagModelSerializer,
)

# Filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

# Models
from cctart.art_pieces.models import (
    ArtPiece,
    ArtPieceDetail,
    ArtPieceTag
)

# Permissions
from cctart.users.permissions import (
    IsAdmin,
    IsAccountOwner,
)
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
)

# Utilities
import json

class ArtPieceViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    """Art Pieces view set."""

    serializer_class = ArtPieceModelSerializer
    lookup_field = 'slug_name'

    # Filters
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ['name']
    ordering_fields = [
        'price',
        'name',
    ]
    # ordering = ['likes__count']
    filter_fields = ['name', 'price']

    def get_queryset(self):
        """Restrict list to active-only."""

        queryset = ArtPiece.objects.all()
        if self.action == 'list':
            return queryset.filter(deleted=False)
        return queryset

    def get_permissions(self):
        """Assign permissions based on action."""
        if self.action in ['list', 'retrieve']:
            permissions = [AllowAny]
        elif self.action in ['destroy']:
            permissions = [IsAuthenticated, IsAdmin]
        else:
            permissions = [IsAuthenticated]
        return [p() for p in permissions]

    def perform_destroy(self, instance):
        """Disable artist."""
        instance.deleted = True
        instance.save()

    def create(self, request, *args, **kwargs):
        """Handle art pieces creation with details and tags."""
        serializer = AddArtPieceModelSerializer(
            data=json.loads(request.data['data']),
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        artpiece = serializer.save()

        data = self.get_serializer(artpiece).data
        return Response(data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        """Handle update artpiece and add details and tags"""
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = UpdateArtPieceModelSerializer(
            instance,
            data=json.loads(request.data['data']),
            partial=partial
        )
        serializer.is_valid(raise_exception=True)
        artpiece = serializer.save()

        data = self.get_serializer(artpiece).data
        return Response(data, status=status.HTTP_200_OK)


class ArtPieceTagViewSet(
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    """Art Pieces Tag view set."""

    serializer_class = ArtPieceTagModelSerializer

    def dispatch(self, request, *args, **kwargs):
        """Verify that the art piece exists."""
        slug_name = kwargs['slug_name']
        self.art_piece = get_object_or_404(
            ArtPiece,
            slug_name=slug_name
        )
        return super(ArtPieceTagViewSet, self).dispatch(request, *args, **kwargs)


    def get_queryset(self):
        """Restrict list to tags of the art piece given in the slug name"""
        return ArtPieceTag.objects.filter(art_piece=self.art_piece)

class ArtPieceDetailViewSet(
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    """Art Pieces Detail view set."""

    serializer_class = ArtPieceDetailModelSerializer

    def dispatch(self, request, *args, **kwargs):
        """Verify that the art piece exists."""
        slug_name = kwargs['slug_name']
        self.art_piece = get_object_or_404(
            ArtPiece,
            slug_name=slug_name
        )
        return super(ArtPieceDetailViewSet, self).dispatch(request, *args, **kwargs)


    def get_queryset(self):
        """Restrict list to details of the art piece given in the slug name."""
        return ArtPieceDetail.objects.filter(art_piece=self.art_piece)
