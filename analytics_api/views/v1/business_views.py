from rest_framework import viewsets
from analytics.models import Business
from analytics_api.serializers.business_serializers import (
    BusinessRetrieveSerializer,
    BusinessCreateSerializer,
)


class BusinessViewSet(viewsets.ModelViewSet):
    queryset = Business.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return BusinessCreateSerializer
        return BusinessRetrieveSerializer
