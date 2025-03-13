from rest_framework import viewsets
from analytics.models import Post
from analytics_api.serializers.post_serializers import (
    PostRetrieveSerializer,
    PostCreateSerializer,
)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return PostCreateSerializer
        return PostRetrieveSerializer
