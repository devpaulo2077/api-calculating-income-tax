from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(["GET"])
def index(request):
    if request.method == "GET":
        return Response(status.HTTP_200_OK)
    return Response(status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def calculate(request, value, deductions="0"):
    if request.method == "GET":
        value = float(value)
        deductions = float(deductions)
        calculate_base = value - deductions

        if value <= 22847.76:
            return Response("Isento")

        elif value <= 33919.80:
            discount = 1712.81
            percentage = 0.075 
            tax = (calculate_base * percentage) - discount
            return Response(tax)

        elif value <= 45012.60:
            discount = 4257.57 
            percentage = 0.15 
            tax = (calculate_base * percentage) - discount
            return Response(tax)

        elif value <= 55976.16:
            discount = 7633.51
            percentage = 0.225
            tax = (calculate_base * percentage) - discount
            return Response(tax)

        elif value > 55976.16:
            discount = 10432.32
            percentage = 0.275
            tax = (calculate_base * percentage) - discount
            return Response(tax)

        else:
            return Response(status.HTTP_404_NOT_FOUND)