from rest_framework import serializers
from analytics.models import Insight


class InsightRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insight
        fields = [
            "id",
            "business",
            "post",
            "analysis_type",
            "raw_data",
            "insights",
            "created_at",
        ]


class InsightCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insight
        fields = ["business", "post", "analysis_type", "raw_data", "insights"]
