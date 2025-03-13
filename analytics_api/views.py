from django.shortcuts import render
from django.http import JsonResponse
from analytics.services.analytics import process_analysis


def analyze_data(request):
    """Endpoint para exponer análisis de datos"""
    data = {"message": "Processing AI data"}
    result = process_analysis(data)
    return JsonResponse(result)
