"""Artists serializer."""

# Django REST Framework
from rest_framework import serializers

# Models
from cctart.artists.models import Artist

class ArtistModelSerializer(serializers.ModelSerializer):
    """Artist model serializer."""

    class Meta:
        """Meta class."""

        model = Artist
        fields = (
            'slug_name',
            'first_name',
            'last_name',
            'website',
            'email',
            'address',
            'biography',
            'photo',
        )

        read_only_fields = ('slug_name',)
