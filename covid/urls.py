from rest_framework.routers import DefaultRouter
from .api import PostViewSet, CategoryViewSet

default_router = DefaultRouter()

default_router.register("post", PostViewSet, basename="create-post")
default_router.register("category", CategoryViewSet, basename="category")

urlpatterns = default_router.urls