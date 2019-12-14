"""cctart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Django
from django.contrib import admin
from django.urls import path, include

# Django REST Framework
from rest_framework_simplejwt.views import TokenRefreshView

# Custom Token
from config.customtoken import CustomTokenObtainPairView

urlpatterns = [
    # Django Admin
    path('admin/', admin.site.urls),

    # Django REST Framework
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Apps
    path(
        '',
        include(
            ('cctart.artists.urls', 'artists'),
            namespace='artists'
        )
    ),
    path(
        '',
        include(
            ('cctart.categories.urls', 'categories'),
            namespace='categories'
        )
    ),
    path(
        '',
        include(
            ('cctart.art_pieces.urls', 'art-pieces'),
            namespace='art-pieces'
        )
    ),
    path(
        '',
        include(
            ('cctart.events.urls', 'events'),
            namespace='events'
        )
    ),
    path(
        '',
        include(
            ('cctart.users.urls', 'users'),
            namespace='users'
        )
    ),
    path(
        '',
        include(
            ('cctart.orders.urls', 'orders'),
            namespace='orders'
        )
    ),

]
