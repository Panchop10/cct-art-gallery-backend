"""Order models"""

# Django
from django.db import models

# Utilities
from cctart.utils.models import CCTArtGalleryModel

class Order(CCTArtGalleryModel):
    """Order model."""

    user = models.ForeignKey(
        'users.User',
        on_delete=models.PROTECT,
        related_name='orders'
    )

    date = models.DateTimeField(auto_now_add=True)

    total = models.PositiveIntegerField()

    payment_method = models.CharField(max_length=150)

    delivered = models.BooleanField(
        default=False,
        help_text=(
            'Tell us if a order was delivered or not'
        )
    )

    def __str__(self):
        """Return order"""
        return self.user.username + ": €" + self.total + " at: " + self.date
