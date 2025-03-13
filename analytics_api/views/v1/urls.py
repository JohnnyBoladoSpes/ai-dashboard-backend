from django.urls import path, include
from rest_framework.routers import DefaultRouter
from analytics_api.views.v1.business_views import BusinessViewSet
from analytics_api.views.v1.post_views import PostViewSet
from analytics_api.views.v1.engagement_views import EngagementMetricViewSet
from analytics_api.views.v1.insight_views import InsightViewSet

router = DefaultRouter()
router.register(r"businesses", BusinessViewSet)
router.register(r"posts", PostViewSet)
router.register(r"engagements", EngagementMetricViewSet)
router.register(r"insights", InsightViewSet)

urlpatterns = router.urls
