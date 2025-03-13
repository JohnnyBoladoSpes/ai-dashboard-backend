from rest_framework import serializers
from analytics.models import Post


class PostRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "business", "content", "created_at"]


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["business", "content"]
