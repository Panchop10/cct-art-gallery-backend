"""Order views."""

# Django REST Framework
from rest_framework import viewsets, mixins, status
from rest_framework.response import Response

# Serializers
from cctart.orders.serializers import (
    OrderModelSerializer,
    UpdateOrderModelSerializer,
    AddOrderModelSerializer
)

# Models
from cctart.orders.models import Order

class OrderViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """Order view set."""

    serializer_class = OrderModelSerializer
    queryset = Order.objects.all()
    lookup_field = 'pk'

    def create(self, request, *args, **kwargs):
        """Handle order creation with art pieces."""
        serializer = AddOrderModelSerializer(
            data=request.data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        order = serializer.save()

        data = self.get_serializer(order).data
        return Response(data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        """Handle update order status"""
        instance = self.get_object()
        serializer = UpdateOrderModelSerializer(
            instance,
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        order = serializer.save()

        data = self.get_serializer(order).data
        return Response(data, status=status.HTTP_200_OK)
