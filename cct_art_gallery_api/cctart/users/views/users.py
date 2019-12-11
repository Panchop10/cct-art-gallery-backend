"""Categories views."""

# Django REST Framework
from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

# Serializers
from cctart.users.serializers import (
    UserModelSerializer,
    UserLikesViewSet,
    AddUserLikesViewSet,
    UserOrdersViewSet
)

# Models
from cctart.users.models import User
from cctart.art_pieces.models import ArtPiece

class UserViewSet(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    """User view set."""

    serializer_class = UserModelSerializer
    lookup_field = 'username'

    def get_queryset(self):
        """Restrict list to verified users."""

        queryset = User.objects.all()
        if self.action == 'list':
            return queryset.filter(is_verified=True)
        return queryset


class UserLikesViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    """User Likes Art Pieces view set."""

    serializer_class = UserLikesViewSet
    lookup_field = "slug_name"

    def dispatch(self, request, *args, **kwargs):
        """Verify that the user exists."""
        username = kwargs['username']
        self.user = get_object_or_404(
            User,
            username=username
        )
        return super(UserLikesViewSet, self).dispatch(request, *args, **kwargs)


    def get_queryset(self):
        """Restrict list to artpieces included in the instance user."""
        return self.user.artpieces.all()

    def perform_destroy(self, instance):
        """Remove artpiece from likes."""
        #import ipdb; ipdb.set_trace()
        self.user.artpieces.remove(instance)
        self.user.save()

    def create(self, request, *args, **kwargs):
        """Handle like event."""
        #import ipdb; ipdb.set_trace()
        serializer = AddUserLikesViewSet(
            data=request.data,
            context={'request': request, 'user': self.user}
        )
        serializer.is_valid(raise_exception=True)
        artpiece = serializer.save()
        data = self.get_serializer(artpiece).data
        return Response(data, status=status.HTTP_201_CREATED)

class UserOrderViewSet(mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """User Order view set."""

    serializer_class = UserOrdersViewSet
    lookup_field = "pk"

    def dispatch(self, request, *args, **kwargs):
        """Verify that the user exists."""
        username = kwargs['username']
        self.user = get_object_or_404(
            User,
            username=username
        )
        return super(UserOrderViewSet, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        """Restrict list to orders included in the instance user."""
        return self.user.orders.all()
