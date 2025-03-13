from rest_framework import serializers
from analytics.models import EngagementMetric


class EngagementRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = EngagementMetric
        fields = ["id", "post", "likes", "comments", "shares", "collected_at"]


class EngagementCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = EngagementMetric
        fields = ["post", "likes", "comments", "shares"]
