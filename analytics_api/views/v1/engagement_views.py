from rest_framework import viewsets
from analytics.models import EngagementMetric
from analytics_api.serializers.engagement_serializers import (
    EngagementRetrieveSerializer,
    EngagementCreateSerializer,
)


class EngagementMetricViewSet(viewsets.ModelViewSet):
    queryset = EngagementMetric.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return EngagementCreateSerializer
        return EngagementRetrieveSerializer
