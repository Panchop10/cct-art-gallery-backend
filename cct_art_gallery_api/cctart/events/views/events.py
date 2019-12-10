"""Categories views."""

# Django REST Framework
from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

# Serializers
from cctart.events.serializers import (
    EventModelSerializer,
    AddEventModelSerializer,
    UpdateEventModelSerializer,
    SingleArtPieceModelSerializer
)

# Models
from cctart.events.models import Event
from cctart.art_pieces.models import ArtPiece

class EventViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    """Category view set."""

    serializer_class = EventModelSerializer
    lookup_field = 'slug_name'

    def get_queryset(self):
        """Restrict list to non-deleted."""

        queryset = Event.objects.all()
        if self.action == 'list':
            return queryset.filter(deleted=False)
        return queryset

    def perform_destroy(self, instance):
        """Disable event."""
        instance.deleted = True
        instance.save()

    def create(self, request, *args, **kwargs):
        """Handle event creation with art pieces"""
        serializer = AddEventModelSerializer(
            data=request.data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        event = serializer.save()

        data = self.get_serializer(event).data
        return Response(data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        """Handle update event and add new artpieces to event"""
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = UpdateEventModelSerializer(
            instance,
            data=request.data,
            partial=partial
        )
        serializer.is_valid(raise_exception=True)
        event = serializer.save()

        data = self.get_serializer(event).data
        return Response(data, status=status.HTTP_200_OK)


class EventArtPieceViewSet(
                    mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    """Event Art Pieces view set."""

    serializer_class = SingleArtPieceModelSerializer
    lookup_field = "slug_name"

    def dispatch(self, request, *args, **kwargs):
        """Verify that the art piece exists."""
        slug_name = kwargs['slug_name_event']
        self.event = get_object_or_404(
            Event,
            slug_name=slug_name
        )
        return super(EventArtPieceViewSet, self).dispatch(request, *args, **kwargs)


    def get_queryset(self):
        """Restrict list to artpieces included in the instance event."""
        return ArtPiece.objects.filter(events=self.event)

    def perform_destroy(self, instance):
        """Remove artpiece from event."""
        self.event.artpieces.remove(instance)
        self.event.save()
