from rest_framework import serializers
from .models import Post, Category, User, Address
from .services import update_object


class UserCreateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    class Meta:
        model = User
        fields = (
            "name",
            "email",
            "mobile"
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "name",
        )


class AddressCreateSerializer(serializers.ModelSerializer):
    line_2 = serializers.CharField(required=False)
    landmark = serializers.CharField(required=False)
    class Meta:
        model = Address
        fields = (
            "line_1",
            "line_2",
            "city",
            "state",
            "landmark",
            "pincode",
        )


class PostCreateSerializer(serializers.ModelSerializer):
    user = UserCreateSerializer(required=True)
    address = AddressCreateSerializer(required=True)
    categories = serializers.SlugRelatedField(
        many=True,
        queryset=Category.objects.all(),
        slug_field="name",
        required=True
    )

    class Meta:
        model = Post
        fields = (
            "user",
            "address",
            "categories",
            "message",
            "like",
            "dislike",
        )

    def create(self, validated_data):
        user = validated_data.pop("user", {})
        categories = validated_data.pop('categories', [])
        address = validated_data.pop("address", {})

        post_obj = Post.objects.create(**validated_data)

        if user:
            user_serializer = UserCreateSerializer(data=user)
            user_serializer.is_valid(raise_exception=True)
            user_obj = user_serializer.save()
            post_obj.user = user_obj

        if address:
            address_serializer = AddressCreateSerializer(data=address)
            address_serializer.is_valid(raise_exception=True)
            address_obj = address_serializer.save()
            post_obj.address = address_obj

        for category in categories:
            post_obj.category.add(category)

        post_obj.save()

        return post_obj

    def update(self, instance, validated_data):
        post_obj = instance()

        update_object(post_obj, validated_data)

        return post_obj


class PostDetailSerializer(serializers.ModelSerializer):
    user = UserCreateSerializer(read_only=True)
    address = AddressCreateSerializer(read_only=True)
    is_liked = serializers.SerializerMethodField()
    is_disliked = serializers.SerializerMethodField()
    is_reported = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = (
            "id",
            "user",
            "address",
            "message",
            "like",
            "dislike",
            "category",
            "is_liked",
            "is_disliked",
            "is_reported",
        )

    def get_is_liked(self, obj):
        return False

    def get_is_disliked(self, obj):
        return False

    def get_is_reported(self, obj):
        return False

