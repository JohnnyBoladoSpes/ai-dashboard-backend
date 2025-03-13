from rest_framework import serializers
from analytics.models import Business


class BusinessRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = ["id", "name", "industry", "created_at"]


class BusinessCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = ["name", "industry"]
