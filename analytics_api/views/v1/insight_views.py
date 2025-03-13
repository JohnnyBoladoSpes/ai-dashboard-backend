from rest_framework import viewsets
from analytics.models import Insight
from analytics_api.serializers.insight_serializers import (
    InsightRetrieveSerializer,
    InsightCreateSerializer,
)


class InsightViewSet(viewsets.ModelViewSet):
    queryset = Insight.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return InsightCreateSerializer
        return InsightRetrieveSerializer
