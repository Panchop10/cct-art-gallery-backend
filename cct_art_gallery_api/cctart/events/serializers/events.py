"""Event serializer."""

# Django REST Framework
from rest_framework import serializers

# Models
from cctart.events.models import Event
from cctart.art_pieces.models import ArtPiece

# Serializers
from cctart.categories.serializers import CategoryModelSerializer
from cctart.artists.serializers import ArtistModelSerializer

class SingleArtPieceModelSerializer(serializers.ModelSerializer):
    """Single Art Piece model serializer."""

    category = CategoryModelSerializer(many=False)
    artist = ArtistModelSerializer(many=False)

    class Meta:
        """Meta class."""

        model = ArtPiece
        fields = (
            'slug_name',
            'name',
            'description',
            'price',
            'photo',
            'artist',
            'category'
        )

        read_only_fields = ('slug_name',)

class EventModelSerializer(serializers.ModelSerializer):
    """Event model serializer."""

    artpieces = SingleArtPieceModelSerializer(many=True, required=False)

    class Meta:
        """Meta class."""

        model = Event
        fields = (
            'slug_name',
            'name',
            'date',
            'description',
            'location',
            'photo',
            'finished',
            'artpieces'
        )

        read_only_fields = ('slug_name',)


class AddEventModelSerializer(serializers.ModelSerializer):
    """Add Event model serializer."""

    artpieces = serializers.SlugRelatedField(
        slug_field='slug_name',
        queryset=ArtPiece.objects.filter(),
        many=True,
        allow_null=True
    )

    class Meta:
        """Meta class."""

        model = Event
        fields = (
            'name',
            'date',
            'description',
            'location',
            'photo',
            'artpieces'
        )

    def create(self, data):
        """Create event with art pieces."""
        artpieces_data = data.pop('artpieces')

        event = Event.objects.create(**data)

        for artpiece_data in artpieces_data:
            event.artpieces.add(artpiece_data)

        return event


class UpdateEventModelSerializer(serializers.ModelSerializer):
    """Update Event model serializer."""

    artpieces = serializers.SlugRelatedField(
        slug_field='slug_name',
        queryset=ArtPiece.objects.filter(),
        many=True,
        allow_null=True,
        required=False
    )

    class Meta:
        """Meta class."""

        model = Event
        fields = (
            'name',
            'date',
            'description',
            'location',
            'photo',
            'artpieces'
        )

    def update(self, instance, data):
        """Update event."""
        event = instance

        if 'artpieces' in data:
            artpieces_data = data.pop('artpieces')
            for artpiece_data in artpieces_data:
                event.artpieces.add(artpiece_data)

        return super(UpdateEventModelSerializer, self).update(instance, data)
