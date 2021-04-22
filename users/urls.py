from rest_framework.routers import DefaultRouter

from .auth.api import AuthViewSet

default_router = DefaultRouter()

default_router.register("auth", AuthViewSet, basename="auth")

urlpatterns = default_router.urls
