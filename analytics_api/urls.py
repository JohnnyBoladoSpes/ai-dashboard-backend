from django.urls import path, include

urlpatterns = [
    path("v1/", include("analytics_api.views.v1.urls")),
]
