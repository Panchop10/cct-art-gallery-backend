"""Art Piece serializer."""

# Django REST Framework
from rest_framework import serializers

# Models
from cctart.art_pieces.models import ArtPiece
from cctart.art_pieces.models import ArtPieceDetail
from cctart.art_pieces.models import ArtPieceTag
from cctart.artists.models import Artist
from cctart.categories.models import Category
from cctart.events.models import Event
from cctart.users.models import User
from cctart.orders.models import Order

# Serializers
from cctart.art_pieces.serializers.details import ArtPieceDetailModelSerializer
from cctart.art_pieces.serializers.tags import ArtPieceTagModelSerializer
from cctart.categories.serializers import CategoryModelSerializer
from cctart.artists.serializers import ArtistModelSerializer

class SingleEventModelSerializer(serializers.ModelSerializer):
    """Single event model serializer."""

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
        )

        read_only_fields = ('slug_name',)

class SingleUserModelSerializer(serializers.ModelSerializer):
    """Single user model serializer."""

    class Meta:
        """Meta class."""

        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'photo'
        )

        read_only_fields = ('username',)


class SingleOrderModelSerializer(serializers.ModelSerializer):
    """Single order model serializer."""

    user = SingleUserModelSerializer(many=False)

    class Meta:
        """Meta class."""

        model = Order
        fields = (
            'pk',
            'user',
            'date',
            'total',
            'payment_method',
            'delivered',
        )

        read_only_fields = ('user',)

class ArtPieceModelSerializer(serializers.ModelSerializer):
    """Art Piece model serializer."""

    category = CategoryModelSerializer(many=False)
    artist = ArtistModelSerializer(many=False)
    order = SingleOrderModelSerializer(many=False)

    details = ArtPieceDetailModelSerializer(many=True)
    tags = ArtPieceTagModelSerializer(many=True)
    events = serializers.SerializerMethodField()
    likes = serializers.SerializerMethodField()

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
            'category',
            'order',
            'details',
            'tags',
            'likes',
            'events'
        )
        depth = 1

        read_only_fields = ('slug_name', 'likes', 'events')

    def get_events(self, obj):
        events = Event.objects.filter(artpieces=obj, deleted=False)
        serializer = SingleEventModelSerializer(instance=events, many=True)
        return serializer.data

    def get_likes(self, obj):
        users = User.objects.filter(artpieces=obj)
        serializer = SingleUserModelSerializer(instance=users, many=True)
        return serializer.data


class AddArtPieceModelSerializer(serializers.ModelSerializer):
    """Add Art Piece model serializer."""

    category = serializers.SlugRelatedField(
        slug_field='slug_name',
        queryset=Category.objects.filter()
    )
    artist = serializers.SlugRelatedField(
        slug_field='slug_name',
        queryset=Artist.objects.filter()
    )

    details = ArtPieceDetailModelSerializer(many=True)
    tags = ArtPieceTagModelSerializer(many=True)

    class Meta:
        """Meta class."""

        model = ArtPiece
        fields = (
            'name',
            'description',
            'price',
            'photo',
            'artist',
            'category',
            'order',
            'details',
            'tags'
        )

    def create(self, data):
        """Create art pieces with details, tags, artist."""

        details_data = data.pop('details')
        tags_data = data.pop('tags')
        try:
            data['photo'] = self.context['request'].data['photo']
        except:
            pass

        art_piece = ArtPiece.objects.create(**data)

        for detail_data in details_data:
            ArtPieceDetail.objects.create(art_piece=art_piece, **detail_data)

        for tag_data in tags_data:
            ArtPieceTag.objects.create(art_piece=art_piece, **tag_data)

        return art_piece


class UpdateArtPieceModelSerializer(serializers.ModelSerializer):
    """Update Art Piece model serializer."""

    category = serializers.SlugRelatedField(
        slug_field='slug_name',
        queryset=Category.objects.filter(),
        required = False
    )
    artist = serializers.SlugRelatedField(
        slug_field='slug_name',
        queryset=Artist.objects.filter(),
        required = False
    )

    details = ArtPieceDetailModelSerializer(many=True, required=False)
    tags = ArtPieceTagModelSerializer(many=True, required=False)

    class Meta:
        """Meta class."""

        model = ArtPiece
        fields = (
            'name',
            'description',
            'price',
            'photo',
            'artist',
            'category',
            'order',
            'details',
            'tags'
        )

    def update(self, instance, data):
        """Update art pieces."""
        art_piece = instance

        if 'details' in data:
            details_data = data.pop('details')
            for detail_data in details_data:
                ArtPieceDetail.objects.create(art_piece=art_piece, **detail_data)

        if 'tags' in data:
            tags_data = data.pop('tags')
            for tag_data in tags_data:
                ArtPieceTag.objects.create(art_piece=art_piece, **tag_data)

        return super(UpdateArtPieceModelSerializer, self).update(instance, data)
