from django.urls import path
from analytics_api import views

urlpatterns = [
    path("analyze/", views.analyze_data, name="analyze_data"),
]
