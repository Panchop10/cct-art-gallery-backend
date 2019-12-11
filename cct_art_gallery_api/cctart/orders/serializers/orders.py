"""Orders serializer."""

# Django REST Framework
from rest_framework import serializers

# Utils
from django.utils import timezone

# Models
from cctart.orders.models import Order
from cctart.users.models import User
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

class OrderModelSerializer(serializers.ModelSerializer):
    """Order model serializer."""

    user = SingleUserModelSerializer(many=False)
    artpieces = SingleArtPieceModelSerializer(many=True)

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
            'artpieces'
        )

        read_only_fields = ('user',)


class UpdateOrderModelSerializer(serializers.ModelSerializer):
    """Order model serializer."""

    class Meta:
        """Meta class."""

        model = Order
        fields = (
            'pk',
            'delivered',
        )

        read_only_fields = ('pk',)

class AddOrderModelSerializer(serializers.ModelSerializer):
    """Add order model serializer."""

    user = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.filter()
    )
    artpieces = serializers.SlugRelatedField(
        slug_field='slug_name',
        queryset=ArtPiece.objects.filter(),
        many=True
    )

    class Meta:
        """Meta class."""

        model = Order
        fields = (
            'user',
            'total',
            'payment_method',
            'artpieces'
        )


    def create(self, data):
        """Create art pieces with details, tags, artist."""

        artpieces_data = data.pop('artpieces')
        data["date"] = timezone.now()

        order = Order.objects.create(**data)

        for artpiece_data in artpieces_data:
            order.artpieces.add(artpiece_data)

        return order
