from django.http import JsonResponse
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser, MultiPartParser

from base import response
from base.viewsets import GenericViewSet as ViewSet

from .models import Post, Category
from .serializers import PostCreateSerializer, CategorySerializer, PostDetailSerializer


class PostViewSet(ViewSet, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.ListModelMixin):
    serializer_class = PostCreateSerializer
    parser_classes = (
        MultiPartParser,
        JSONParser
    )
    queryset = Post.objects.all()

    def create(self, request, *args, **kwargs):
        
        serializer = PostCreateSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        post_obj = serializer.save()

        return response.Created(
            {
                "id": post_obj.id,
                "response": True
            }
        )

    @action(methods=['PATCH'], detail=True)
    def update_post(self, request, pk=None):
        post_obj = self.get_object

        post_serializer = PostCreateSerializer(
            instance=post_obj,
            data=request.data,
            partial=True
        )

        post_serializer.is_valid(raise_exception=True)
        post_obj = post_serializer.save()

        return response.Ok(
            {
                "id": post_obj.id,
                "response": True
            }
        )

    def get_serializer_class(self, *args, **kwargs):
        if self.action == "list":
            return PostDetailSerializer


class CategoryViewSet(ViewSet):
    serializer_class = CategorySerializer
    parser_classes = (
        MultiPartParser,
        JSONParser
    )
    queryset = Category.objects.all()

    @action(methods=['GET'], detail=False)
    def categories(self, request, pk=None):
        categories = Category.objects.values("name")

        return response.Ok(categories)

